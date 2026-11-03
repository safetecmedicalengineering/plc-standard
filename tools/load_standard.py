"""Print one file of the general standard for a SessionStart hook.

Usage:
    python load_standard.py <file>    print standard/<file> (Claude Code adds hook stdout to the context)
    python load_standard.py --check   check that every standard file fits the hook output limit

Claude Code caps the output of one hook at 10,000 characters. Longer output is not shown in the
context, only saved to a file, so every standard file is loaded by its own hook and must stay below
LIMIT. The first file also prints where the plugin and its tools are.

Standard library only.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STANDARD = ROOT / "standard"
LIMIT = 9000  # margin below the 10,000 character cap for the heading lines


def version():
    manifest = ROOT / ".claude-plugin" / "plugin.json"
    return json.loads(manifest.read_text(encoding="utf-8-sig")).get("version", "?")


def check():
    files = sorted(STANDARD.glob("*.md"))
    too_long = []
    for f in files:
        n = len(f.read_text(encoding="utf-8-sig"))
        print(f"{f.name}: {n} znaků")
        if n > LIMIT:
            too_long.append(f.name)
    hooks = (ROOT / "hooks" / "hooks.json").read_text(encoding="utf-8-sig")
    missing = [f.name for f in files if f"load_standard.py\\\" {f.name}" not in hooks]
    for name in too_long:
        print(f"CHYBA: {name} je delší než {LIMIT} znaků, rozděl ho.")
    for name in missing:
        print(f"CHYBA: {name} nemá hook v hooks/hooks.json.")
    return 1 if too_long or missing else 0


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if not argv:
        print(__doc__)
        return 1
    if argv[0] == "--check":
        return check()
    path = STANDARD / argv[0]
    text = path.read_text(encoding="utf-8-sig").rstrip()
    if path.name.startswith("01-"):
        tools = (ROOT / "tools").as_posix()
        print(f"# Obecný standard plc-standard {version()}")
        print(f"Plugin: {ROOT.as_posix()}")
        print(f"Snímek exportu: python \"{tools}/vci_snapshot.py\" <kořen projektu>")
        print(f"Agentům plc-coder a plc-reviewer předej cestu ke standardu: {STANDARD.as_posix()}")
        print()
    print(f"<!-- plc-standard/{path.name} -->")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
