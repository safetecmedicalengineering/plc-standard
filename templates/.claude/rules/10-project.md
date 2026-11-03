# Projektové invarianty

Schválené záměry tohoto projektu. Mění se jen rozhodnutím, ne po refreshi VCI.
Konkrétní bloky, volání a zápisy ber ze snímku docs/generated/INVENTORY.md.
Strojově kontrolovatelné invarianty jsou v docs/invariants.json (kontroluje vci_snapshot.py).

## Workspace
- Export: `{{PLC}}/` (bloky, UDT, tagy, TO); konfigurace VCI: `.vci/`. Podrobnosti v docs/WORKSPACE.md.

## Symboly a dodavatelský kód
- {{Veřejné symboly s překlepy, které se musí zachovat.}}
- {{Dodavatelské bloky (prefix, výrobce) – reference, neupravovat bez zadání.}}

## Standard stanic
- {{Bloky řízení stanic a sekvencí, datové typy stanic, režimy, šablona nové stanice.}}

## Konvence pojmenování
- {{Prefixy globálních DB, stanic, parametrů, lokálních proměnných.}}

## Vlastnictví výstupů
- {{Výstupy, které smí zapisovat jen jeden blok (doplnit i do docs/invariants.json).}}

## Bezpečnost
- {{Které REGIONy nebo bloky jsou jen diagnostika a které jsou certifikovaná safety funkce.}}
