# VCI, import a ověření

- docs/WORKSPACE.md projektu popisuje skutečnou složku, formáty a mapování skupin.
- Konfiguraci VCI (.vci/) neměň; ovlivňuje exportní workflow.
- Nové bloky ukládej do existující skupiny; novou cestu nezakládej bez ověření.
- Živé VCI soubory získávej skutečným exportem z příslušného TIA projektu.
- Obsah, který export neobsahuje (typicky UDT, tag tabulky, TO, HW konfigurace), nevymýšlej.
- Zachovej jména, cesty, formát, atributy, kódování a doprovodné soubory exportu.
- Pokud existují .s7res, .libinfo, .libint nebo .liblink, zachovej jejich vazby.
- Před změnou porovnej TIA, disk a Git. Konflikty vyřeš před přenosem.
  Bez Gitu ulož původní stav souboru před úpravou.
- Jeden objekt se v daný okamžik edituje jen na jedné straně synchronizace.
- Git checkout nebo změna souboru na disku sama o sobě není importem do TIA.
- Před importem uveď přesné dotčené objekty a závislosti; neimportuj vše bez rozmyslu.
- Po importu zkompiluj dotčené PLC software a posuď i relevantní varování.
- Opravuj podle skutečných hlášení překladače dané revize.
- Po kompilaci stále zbývá funkční ověření; textová kontrola nenahrazuje ani jedno.
- Po ověření znovu exportuj do workspace, spusť vci_snapshot.py a projdi diff před commitem.
- Verzionovaný export nenahrazuje archiv celého projektu TIA.

## Po refreshi VCI
1. Spusť `vci_snapshot.py <projekt>` – přegeneruje docs/generated/INVENTORY.md a zkontroluje invarianty.
2. Porušení invariantu (exit 2) řeš jako nález, ne úpravou invariants.json.
3. Projdi docs/PROJECT.md a docs/OPEN_ITEMS.md proti novému snímku; uzavřené body označ datem.
