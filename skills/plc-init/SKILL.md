---
name: plc-init
description: Založí v PLC projektu (VCI workspace TIA Portal) kostru podle plc-standard – CLAUDE.md, projektové invarianty, docs/, nastavení pluginu, lokální git a první snímek exportu. Použij, když uživatel zakládá nový projekt nebo připojuje existující VCI workspace ke standardu.
---

# Založení PLC projektu

Kořen projektu = kořen VCI workspace (aktuální pracovní složka, pokud uživatel neřekne jinak).
Existující soubory nikdy nepřepisuj.

1. **Zjisti stav.** Vypiš obsah kořene. Najdi složku exportu PLC: podsložka, která obsahuje
   `Program blocks/` (např. `50A1`). Zjisti, jestli existuje `.vci/` a `.git/`.
   - Žádný export ani `.vci/`: řekni, že VCI workspace zatím není nastavený, a odkaž na návod.
     Pokračuj, jen když to uživatel chce (kostra může vzniknout před prvním exportem).
   - Víc složek s `Program blocks/`: zeptej se, která je ta pravá.
2. **Zeptej se** na název projektu (výchozí: název složky) a krátký popis stroje.
   Pokud složku exportu nešlo zjistit, zeptej se i na ni.
3. **Kostra.** Spusť:
   `python "${CLAUDE_PLUGIN_ROOT}/tools/plc_init.py" "<kořen>" "<složka PLC>" "<název>"`
   Do `CLAUDE.md` pak doplň popis stroje místo řádku `{{POPIS …}}`.
4. **Git.** Pokud `.git/` neexistuje: `git init`, pak `git config core.autocrlf false`
   (VCI soubory mají CRLF a BOM, git je nesmí měnit). Pokud existuje, jen ověř `core.autocrlf`
   a případný rozdíl nahlas, neměň ho bez souhlasu.
5. **Snímek.** `python "${CLAUDE_PLUGIN_ROOT}/tools/vci_snapshot.py" "<kořen>"`
   (jen když export existuje). Exit 2 = porušený invariant, nahlas jako nález.
6. **První commit** – jen se souhlasem uživatele. Do commitu patří kostra, `.vci/`, export a snímek.
7. **Shrnutí.** Vyjmenuj vytvořené a přeskočené soubory a místa `{{…}}`, která musí uživatel
   doplnit (`.claude/rules/10-project.md`, `docs/PROJECT.md`, `docs/WORKSPACE.md`, `docs/OPEN_ITEMS.md`).
   Nabídni, že je po prvním snímku pomůžeš vyplnit z exportu – fakta ber jen z kódu, nic nevymýšlej.
