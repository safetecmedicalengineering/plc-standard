# Pracovní cyklus

Jednotný postup práce s Claude Code na PLC projektu Siemens (TIA Portal, VCI).
Pravidla, kterými se Claude řídí, jsou ve `standard/`. Tady je postup pro člověka.

## Cyklus jedné změny
1. **Synchronizace.** V TIA exportuj přes VCI do workspace. Claudovi napiš „synchronizováno“.
   Claude projde `git status`, `git diff` a přegeneruje snímek (`docs/generated/INVENTORY.md`).
   Tvoje změny z TIA nejdřív vyjmenuje a navazuje na ně.
2. **Zadání.** Popiš, co chceš změnit. Claude vrátí analýzu, návrh, changelog a otázky.
   Uvádí jednotky a výsledná čísla („6 kapes = 6 kroků“), aby šla chyba výkladu vidět předem.
   Iteruj, dokud changelog nesedí. Bloky se v této fázi neupravují.
3. **Generování.** Až řekneš „generuj“ (nebo „implementuj“), Claude upraví soubory v exportu,
   jen v rozsahu odsouhlaseného changelogu a jen přepisem na místě.
4. **Kontrola.** Řekni „udělej review“. Agent `plc-reviewer` projde změnu proti zadání,
   cyklům, instancím a všem dotčeným linkám.
5. **TIA.** Import přes VCI, kompilace, download. Změna rozhraní FB nebo struktury DB
   znamená download v STOP. Funkční ověření na stroji dělá člověk.
6. **Zpět a commit.** Po kompilaci znovu exportuj, napiš „synchronizováno, porovnej a commitni“.
   Claude porovná export s tím, co vygeneroval, a změnu commitne.

## Brány
- **„generuj“** – bez tohoto slova Claude bloky nemění. Souhlas s návrhem ani odpověď na otázku nestačí.
- **Download do PLC** – dělá vždy člověk. Claude nemá k PLC přístup a nesmí ho mít.

## Nikdy
- `git checkout`, `git restore`, `git stash` ani mazání a nové vytvoření souborů v exportu.
  VCI to může vyhodnotit jako smazaný objekt a synchronizace se rozpadne.
- „Load start values as actual values“ / „Snapshot as actual values“ na DB s instrukcemi MC_*.
  Poškodí instance pohybových instrukcí (chyba 16#800C). Náprava: STOP, přeložit DB, download.
- Ručně editovat `docs/generated/INVENTORY.md` nebo `.vci/`.
- Psát fakta konkrétního stroje do `standard/`. Patří do `.claude/rules/10-project.md` projektu.

## Kde co je v projektu
| Vrstva | Soubor | Kdo ho mění |
|---|---|---|
| Obecný standard | plugin `plc-standard` (tento repozitář) | správce standardu, nová verze |
| Projektové invarianty | `.claude/rules/10-project.md`, `docs/invariants.json` | člověk rozhodnutím |
| Popis projektu | `docs/PROJECT.md`, `docs/WORKSPACE.md`, `docs/OPEN_ITEMS.md` | Claude i člověk |
| Snímek exportu | `docs/generated/INVENTORY.md` | jen `vci_snapshot.py` |
