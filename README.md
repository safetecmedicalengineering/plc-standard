# plc-standard

Obecný standard pro návrh a kontrolu PLC kódu Siemens (SCL, TIA Portal VCI).
Neobsahuje nic specifického pro konkrétní stroj. Projektová fakta patří do projektu.

## Obsah
| Cesta | Co to je | Jak se dostane do projektu |
|---|---|---|
| `standard/*.md` | obecná pravidla (rozsah, styl SCL, runtime, VCI) | `@import` v CLAUDE.md projektu |
| `agents/` | `plc-coder`, `plc-reviewer` | plugin |
| `hooks/hooks.json` | SessionStart: upozorní, když snímek exportu neodpovídá exportu | plugin |
| `tools/vci_snapshot.py` | generátor `docs/generated/INVENTORY.md` + kontrola invariantů | ručně po refreshi VCI |

Pluginy v Claude Code nemohou nést `.claude/rules/`, proto jsou pravidla importována z CLAUDE.md.

## Vrstvy v projektu
1. **Obecný standard** – tento repozitář. Mění se zřídka a vědomě.
2. **Projektové invarianty** – `.claude/rules/10-project.md` a `docs/invariants.json` v projektu.
   Schválené záměry, ručně, mění se jen rozhodnutím.
3. **Snímek exportu** – `docs/generated/INVENTORY.md`, generuje `vci_snapshot.py`. Needitovat.

## Připojení k projektu
CLAUDE.md projektu:
```
@~/Desktop/plc-standard/standard/01-scope.md
@~/Desktop/plc-standard/standard/02-scl-style.md
@~/Desktop/plc-standard/standard/03-runtime.md
@~/Desktop/plc-standard/standard/04-vci.md
```
Claude Code se při prvním načtení zeptá na schválení externích importů.

Plugin (agenti a hook):
```bash
claude plugin marketplace add C:/Users/Simek/Desktop/plc-standard
```
```bash
claude plugin install plc-standard@plc-standard --scope project
```

## Po refreshi VCI
```bash
python ~/Desktop/plc-standard/tools/vci_snapshot.py <projekt>
```
Exit 0 = OK, 2 = porušený invariant (řešit jako nález).

## Požadavky
Python 3.9+, jen standardní knihovna.
