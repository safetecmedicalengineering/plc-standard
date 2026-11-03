# {{PROJECT}} – PLC projekt (Siemens TIA)

{{POPIS – jednou až dvěma větami: stroj, linky, stanice.}}

## Obecný standard
Pravidla obecného standardu vkládá plugin `plc-standard` na začátku každé session.
Ve stejném pluginu jsou agenti `plc-coder`, `plc-reviewer`, kontrola zastaralosti snímku
a nástroj `vci_snapshot.py`. Pracovní cyklus: `WORKFLOW.md` v repozitáři pluginu.

## Tři vrstvy informací
1. Obecný standard – plugin, mimo tento projekt. Projektová fakta do něj nepatří.
2. Projektové invarianty – `.claude/rules/10-project.md`, `docs/invariants.json`. Mění se jen rozhodnutím.
3. Snímek exportu – `docs/generated/INVENTORY.md`. Generuje ho `vci_snapshot.py`, ručně needitovat.

Zdrojem pravdy je export v `{{PLC}}/`. Ruční dokumenty (`docs/PROJECT.md`, `docs/OPEN_ITEMS.md`)
popisují architekturu a otevřené body; konkrétní bloky, volání a zápisy výstupů ber ze snímku.

## Kde co je
- `{{PLC}}/` – export PLC: `Program blocks/`, `PLC data types/`, `PLC tags/`, `Technology objects/`.
  `.vci/` – konfigurace VCI, neměnit.
- `docs/WORKSPACE.md` – formáty, mapování skupin, co export neobsahuje.
- `docs/PROJECT.md` – architektura stroje.
- `docs/OPEN_ITEMS.md` – chybějící podklady a nálezy k ověření (datované).

## Po refreshi VCI
Spusť `vci_snapshot.py` z pluginu (cestu vypíše plugin na začátku session) s kořenem projektu,
pak projdi `docs/PROJECT.md` a `docs/OPEN_ITEMS.md` proti novému snímku.
