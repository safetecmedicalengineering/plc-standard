# plc-standard

Obecný standard pro návrh a kontrolu PLC kódu Siemens (SCL, TIA Portal VCI) s Claude Code.
Neobsahuje nic specifického pro konkrétní stroj. Projektová fakta patří do projektu.

**Návod pro nové uživatele:** https://claude.ai/artifact/BYerrDYGAeBU88TLpZv86V
**Pracovní cyklus:** [WORKFLOW.md](WORKFLOW.md) · **Změny:** [CHANGELOG.md](CHANGELOG.md)

## Instalace
Předpoklady: Claude Code, git, Python 3.9+.

Jednou na počítač:
```bash
claude plugin marketplace add safetecmedicalengineering/plc-standard
```
V každém PLC projektu (terminál ve složce VCI workspace). Plugin se zapne jen pro tento projekt,
ostatní projekty standard nenačítají:
```bash
claude plugin install plc-standard@plc-standard --scope project
```
Nový projekt: pak v Claude Code ve stejné složce spusť `/plc-standard:plc-init`.

## Obsah
| Cesta | Co to je |
|---|---|
| `standard/*.md` | obecná pravidla (rozsah, styl SCL, runtime, VCI); hook je vloží do každé session |
| `agents/` | `plc-coder`, `plc-reviewer` |
| `skills/plc-init/` | `/plc-standard:plc-init` – kostra nového projektu ze `templates/` |
| `hooks/hooks.json` | SessionStart: načte standard, upozorní na zastaralý snímek exportu |
| `tools/vci_snapshot.py` | generátor `docs/generated/INVENTORY.md` a kontrola invariantů |
| `tools/load_standard.py` | výpis standardu pro hook; `--check` ověří délku souborů |
| `tools/plc_init.py` | kopírování šablon (volá ho `/plc-init`) |

## Vrstvy v projektu
1. **Obecný standard** – tento repozitář. Mění se zřídka a vědomě.
2. **Projektové invarianty** – `.claude/rules/10-project.md` a `docs/invariants.json` v projektu.
3. **Snímek exportu** – `docs/generated/INVENTORY.md`, generuje `vci_snapshot.py`. Needitovat.

## Změna standardu
1. Uprav soubory ve `standard/`, `agents/`, `skills/` nebo `templates/`. Žádná fakta konkrétního stroje.
2. `python tools/load_standard.py --check` – každý soubor standardu musí mít méně než 9 000 znaků
   (hook smí vložit nejvýš 10 000) a vlastní hook v `hooks/hooks.json`.
3. Zvyš `version` v `.claude-plugin/plugin.json` a zapiš změnu do `CHANGELOG.md`.
   Bez nové verze si uživatelé změnu nestáhnou.
4. Commit a push.

## Požadavky
Python 3.9+, jen standardní knihovna. Příkaz `python` musí být v PATH.
