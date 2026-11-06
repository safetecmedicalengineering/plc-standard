# Changelog

Po každé nové verzi aktualizuj plugin:
```bash
claude plugin marketplace update plc-standard
```
```bash
claude plugin update plc-standard@plc-standard
```

## 0.2.1 – 2026-11-06
- Trace: ke každé konfiguraci soubor `docs/trace/<název>.txt` k přímému vložení do TIA
  (jeden symbolický název na řádek), popis zvlášť v `docs/TRACE_<téma>.md`.

## 0.2.0 – 2026-11-03
- Standard se načítá z pluginu (hook SessionStart), ne přes `@import` z plochy.
  Řádky `@~/Desktop/plc-standard/...` z CLAUDE.md projektů odstraň.
- Skill `/plc-standard:plc-init` založí kostru nového projektu ze `templates/`.
- `WORKFLOW.md` – jednotný pracovní cyklus a seznam „nikdy“.
- Agenti `plc-coder` a `plc-reviewer` čtou standard ze složky pluginu.
- Instalace z GitHubu `safetecmedicalengineering/plc-standard`.

## 0.1.0 – 2026-10-30
- Obecná pravidla (rozsah, styl SCL, runtime, VCI), agenti `plc-coder` a `plc-reviewer`,
  hook kontroly snímku, `vci_snapshot.py`.
- Pravidla: kriticky posuzovat zadání, vycházet z aktuálního repozitáře,
  bloky generovat jen na výslovný pokyn.
