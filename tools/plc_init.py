"""Create the skeleton of a PLC project from templates/.

Usage:
    python plc_init.py <project_root> <plc_folder> [project_name]

<plc_folder> is the folder of the PLC export in the VCI workspace (e.g. 50A1).
Existing files are never overwritten; they are listed as skipped. An existing
.claude/settings.json only gets the plugin marketplace and enablement added.
Placeholders {{PLC}} and {{PROJECT}} are filled, other {{...}} stay for the user.

Standard library only.
"""

import json
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent.parent / "templates"


def merge_settings(src, dst):
    """Add the marketplace and the plugin to existing settings; other keys stay untouched."""
    template = json.loads(src.read_text(encoding="utf-8"))
    current = json.loads(dst.read_text(encoding="utf-8-sig"))
    added = []
    for key in ("extraKnownMarketplaces", "enabledPlugins"):
        section = current.setdefault(key, {})
        for name, value in template[key].items():
            if name not in section:
                section[name] = value
                added.append(f"{key}.{name}")
    if added:
        dst.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        print(f"doplněno do .claude/settings.json: {', '.join(added)}")
    else:
        print("přeskočeno (už obsahuje plugin): .claude/settings.json")


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8")
    if len(argv) < 2:
        print(__doc__)
        return 1
    root = Path(argv[0]).resolve()
    plc = argv[1]
    project = argv[2] if len(argv) > 2 else root.name
    if not root.is_dir():
        print(f"Složka projektu {root} neexistuje.")
        return 1
    if not (root / plc).is_dir():
        print(f"Upozornění: export {root / plc} zatím neexistuje (VCI ho vytvoří po prvním exportu).")

    for src in sorted(TEMPLATES.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(TEMPLATES)
        dst = root / rel
        if dst.exists() and rel.as_posix() == ".claude/settings.json":
            merge_settings(src, dst)
            continue
        if dst.exists():
            print(f"přeskočeno (existuje): {rel.as_posix()}")
            continue
        text = src.read_text(encoding="utf-8").replace("{{PLC}}", plc).replace("{{PROJECT}}", project)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(text, encoding="utf-8", newline="\n")
        print(f"vytvořeno: {rel.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
