# VCI workspace

Stabilní popis workspace. Počty bloků a seznam souborů jsou ve snímku `docs/generated/INVENTORY.md`.

## Umístění
- Kořen workspace = kořen git repozitáře (složka s `CLAUDE.md`).
- Konfigurace VCI: `.vci/` – neměnit, ovlivňuje exportní workflow VCI.
- Export: `{{PLC}}/` (název PLC), uvnitř `Program blocks/`, `PLC data types/`, `PLC tags/`,
  `Technology objects/`. Struktura složek odpovídá skupinám v TIA, jeden objekt na soubor.

## Exportní formáty
| Objekt | Formát |
|---|---|
| Code blocks – LAD / FBD / STL | `.xml` |
| Code blocks – SCL | `.scl` |
| Code blocks – GRAPH | `.xml` |
| Data blocks | `.db` |
| Safety data blocks (F-DB) | `.xml` |
| PLC data types | `.udt` |
| F-compliant UDT | `.xml` |
| PLC tag tables | `.xml` |
| Technology objects | `.xml` |

## Rozsah exportu
VCI neexportuje HW konfiguraci (HW_ID, telegramy, procesní obrazy, periody OB).
{{Knihovní typy, které jsou v exportu jen jako .liblink.}}

## Mapování skupin
Cesty relativně k `{{PLC}}/Program blocks/`.

| Složka | Obsah |
|---|---|
| {{složka}} | {{obsah}} |

## Kódování
UTF-8 s BOM a CRLF. Při úpravě zachovat.

## Synchronizace
Úprava souboru na disku není importem do TIA. Import, kompilace a zpětný export probíhají v TIA přes VCI.
Workspace je lokální git repozitář (`core.autocrlf=false`, soubory se ukládají beze změny).
Po zpětném exportu z TIA spusť vci_snapshot.py, projdi `git diff` a commitni export spolu se snímkem.
Soubory v `{{PLC}}/` upravovat jen přepisem na místě. Smazání a nové vytvoření souboru
(`git checkout/restore/stash`, uložení přes dočasný soubor) může VCI vyhodnotit jako smazaný objekt.
