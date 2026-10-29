"""Snapshot of a TIA Portal VCI export.

Usage:
    python vci_snapshot.py [project_root]           regenerate docs/generated/INVENTORY.md
    python vci_snapshot.py [project_root] --check   only report whether the snapshot is stale

The project root must contain the export folder (default "Program blocks").
Optional docs/invariants.json declares project rules checked on every run:
    {
      "exportDir": "Program blocks",
      "outputPrefixes": ["q"],
      "outputOwners": [ {"tag": "qxDosingValve*", "owners": ["FC_DosingPulse"]} ]
    }

Standard library only. Read-only towards the export.
"""

import fnmatch
import hashlib
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

INVENTORY = Path("docs/generated/INVENTORY.md")
INVARIANTS = Path("docs/invariants.json")
EXTENSIONS = {".scl", ".db", ".udt", ".awl", ".xml", ".s7dcl", ".s7res"}

RE_DEF = re.compile(r'^\s*(FUNCTION_BLOCK|FUNCTION|ORGANIZATION_BLOCK|DATA_BLOCK|TYPE)\s+"([^"]+)"', re.M)
RE_INSTANCE_OF = re.compile(r'^\s*"([^"]+)"\s*$', re.M)
RE_CALL = re.compile(r'"([^"]+)"(?:\.\w+)?\s*\(')
RE_DECL_TYPE = re.compile(r':\s*(?:Array\s*\[[^\]]*\]\s*of\s*)?"([^"]+)"', re.I)
RE_ASSIGN = re.compile(r'"([^"]+)"\s*:=')
RE_HASH = re.compile(r"<!-- export-hash: ([0-9a-f]+) -->")


def strip_comments(text):
    text = re.sub(r"\(\*.*?\*\)", "", text, flags=re.S)
    return re.sub(r"//[^\n]*", "", text)


def export_hash(export_dir):
    h = hashlib.sha256()
    for f in sorted(export_dir.rglob("*")):
        if f.is_file():
            h.update(f.relative_to(export_dir).as_posix().encode("utf-8"))
            h.update(hashlib.sha256(f.read_bytes()).digest())
    return h.hexdigest()[:16]


def load_invariants(root):
    path = root / INVARIANTS
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8-sig"))
    return {}


def parse(export_dir):
    blocks = {}
    for f in sorted(export_dir.rglob("*")):
        if not f.is_file() or f.suffix.lower() not in EXTENSIONS:
            continue
        text = f.read_text(encoding="utf-8-sig", errors="replace")
        m = RE_DEF.search(text)
        if not m:
            blocks[f.stem] = {"kind": "?", "file": f, "decl": "", "body": ""}
            continue
        head, _, body = text.partition("\nBEGIN")
        info = {"kind": m.group(1), "file": f, "decl": strip_comments(head), "body": strip_comments(body)}
        if m.group(1) == "DATA_BLOCK":
            inst = RE_INSTANCE_OF.search(head)
            info["instanceOf"] = inst.group(1) if inst else None
        blocks[m.group(2)] = info
    return blocks


def build(root, export_dir, inv):
    blocks = parse(export_dir)
    prefixes = tuple(inv.get("outputPrefixes", ["q"]))
    lines = []

    counts = defaultdict(int)
    for b in blocks.values():
        counts[b["kind"]] += 1
    lines.append("## Bloky")
    lines.append(", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
    lines.append("")
    lines.append("| Blok | Typ | Instance FB | Soubor |")
    lines.append("|---|---|---|---|")
    for name, b in sorted(blocks.items(), key=lambda x: str(x[1]["file"]).lower()):
        rel = b["file"].relative_to(root).as_posix()
        lines.append(f"| {name} | {b['kind']} | {b.get('instanceOf') or ''} | {rel} |")

    lines.append("")
    lines.append("## Volání z OB (v pořadí výskytu)")
    for name, b in sorted(blocks.items()):
        if b["kind"] != "ORGANIZATION_BLOCK":
            continue
        calls = []
        for c in RE_CALL.findall(b["body"]):
            if c not in calls:
                calls.append(c)
        lines.append(f"- **{name}**: " + (", ".join(calls) if calls else "(žádná)"))

    lines.append("")
    lines.append("## Multi-instance a instanční DB podle FB")
    users = defaultdict(set)
    for name, b in blocks.items():
        for t in RE_DECL_TYPE.findall(b["decl"]):
            if t in blocks and blocks[t]["kind"] == "FUNCTION_BLOCK":
                users[t].add(name)
        if b.get("instanceOf"):
            users[b["instanceOf"]].add(name + " (DB)")
    for fb in sorted(users):
        lines.append(f"- **{fb}**: " + ", ".join(sorted(users[fb])))

    lines.append("")
    lines.append("## Zápisy výstupů (tagy s prefixem " + ", ".join(prefixes) + ")")
    writers = defaultdict(set)
    for name, b in blocks.items():
        for tag in RE_ASSIGN.findall(b["body"]):
            if tag.startswith(prefixes):
                writers[tag].add(name)
    for tag in sorted(writers):
        lines.append(f"- {tag}: " + ", ".join(sorted(writers[tag])))

    lines.append("")
    lines.append("## Typy použité v deklaracích, které v exportu nejsou")
    missing = set()
    for b in blocks.values():
        for t in RE_DECL_TYPE.findall(b["decl"]):
            if t not in blocks:
                missing.add(t)
    lines.append(", ".join(sorted(missing)) if missing else "(žádné)")

    lines.append("")
    lines.append("## Kontrola invariantů (docs/invariants.json)")
    violations = []
    for rule in inv.get("outputOwners", []):
        owners = set(rule["owners"])
        for tag, ws in writers.items():
            if fnmatch.fnmatchcase(tag, rule["tag"]) and ws - owners:
                violations.append(f"{tag} zapisuje i {', '.join(sorted(ws - owners))} (povoleno: {', '.join(sorted(owners))})")
        for owner in owners:
            if owner not in blocks:
                violations.append(f"vlastník {owner} pro {rule['tag']} v exportu chybí")
    if not inv:
        lines.append("Soubor invariants.json neexistuje.")
    elif violations:
        lines.extend(f"- PORUŠENO: {v}" for v in violations)
    else:
        lines.append("Bez porušení.")
    return lines, violations


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in argv if not a.startswith("--")]
    root = Path(args[0] if args else ".").resolve()
    inv = load_invariants(root)
    export_dir = root / inv.get("exportDir", "Program blocks")
    if not export_dir.is_dir():
        if "--check" in argv:
            return 0  # not a VCI project, the hook stays silent
        print(f"vci_snapshot: export {export_dir} nenalezen")
        return 1
    current = export_hash(export_dir)
    out = root / INVENTORY

    if "--check" in argv:
        stored = RE_HASH.search(out.read_text(encoding="utf-8-sig")) if out.exists() else None
        if not stored:
            print(f"VCI snímek chybí ({INVENTORY.as_posix()}). Spusť vci_snapshot.py před prací s kódem.")
        elif stored.group(1) != current:
            print(f"VCI export se od posledního snímku změnil ({stored.group(1)} -> {current}). "
                  f"{INVENTORY.as_posix()} a docs/ mohou být zastaralé; spusť vci_snapshot.py a zkontroluj docs/PROJECT.md.")
        return 0

    body, violations = build(root, export_dir, inv)
    header = [
        "# Snímek VCI exportu",
        "",
        "Generováno skriptem vci_snapshot.py – needitovat ručně. Zdrojem pravdy je kód v exportu.",
        f"<!-- export-hash: {current} -->",
        f"Vygenerováno: {datetime.now():%Y-%m-%d %H:%M}, otisk exportu `{current}`",
        "",
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(header + body) + "\n", encoding="utf-8")
    print(f"{INVENTORY.as_posix()} aktualizován (otisk {current}, porušení invariantů: {len(violations)})")
    return 2 if violations else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
