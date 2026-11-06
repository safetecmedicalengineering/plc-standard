# VCI, import a ověření

## Vycházej z aktuálního repozitáře
- Před každou analýzou, návrhem, generováním i odpovědí o kódu zjisti aktuální stav: `git status`,
  `git diff` proti poslednímu commitu a otisk exportu (`vci_snapshot.py --check`).
- Kód čti znovu ze souborů. Nespoléhej na to, co bylo v konverzaci nebo v dřívějším návrhu – uživatel
  mohl soubory mezitím změnit v TIA a synchronizovat.
- Základem každé úpravy je aktuální soubor v exportu, nikdy text z paměti, pravidel, dokumentace,
  souhrnu konverzace ani dříve vygenerovaná kopie (scratchpad, drafts/). Ty popisují záměr, ne kód.
  Hotový blok nikdy nekopíruj přes soubor v exportu; upravuj jen konkrétní místa aktuálního souboru.
- Změny od uživatele (necommitnuté nebo nové od minula) nejdřív projdi a vyjmenuj; navazuj na ně,
  nepřepisuj je svou starší verzí.
- Generátor nebo skript stav těsně před zápisem ověří kotvami; když kotva nesedí, nezapisuj a zjisti proč.
- Když se stav změní během práce (nová synchronizace), začni znovu od aktuálního stavu.

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

## Trace pro ověření na stroji
- Když uživatel žádá trace, dodej ke každé konfiguraci soubor, který jde přímo vložit do tabulky
  signálů trace v TIA: `docs/trace/<název>.txt`, UTF-8, jeden signál na řádek, symbolický název
  přesně v syntaxi TIA (`"DB".člen.člen`, `"Tag"`, `"TO".ActualPosition`), bez hlavičky, odrážek,
  číslování a komentářů.
- Každý název ověř v aktuálním exportu (deklarace v bloku, DB, UDT nebo tag tabulce); nevymýšlej.
- Počet signálů drž v limitu CPU (S7-1500 obvykle 16 na konfiguraci); víc rozděl do více souborů.
- Popis dej zvlášť do `docs/TRACE_<téma>.md`: místo záznamu (OB) a perioda, spouštěcí podmínka,
  předběh, délka, tabulka signálů se stejným pořadím jako soubor (jednotka, proč), scénáře a kritéria OK.
- Jednocyklové pulzy zaznamenávej v OB, ve kterém vznikají; jinak je vzorkování mine.

## Po refreshi VCI
1. Spusť `vci_snapshot.py <projekt>` – přegeneruje docs/generated/INVENTORY.md a zkontroluje invarianty.
2. Porušení invariantu (exit 2) řeš jako nález, ne úpravou invariants.json.
3. Projdi docs/PROJECT.md a docs/OPEN_ITEMS.md proti novému snímku; uzavřené body označ datem.
