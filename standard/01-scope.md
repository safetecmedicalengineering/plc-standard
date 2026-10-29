# Rozsah změn a reference

- Zdrojem pravdy je kód v exportu. Dokumenty v docs/ jsou snímek; při rozporu platí kód a rozpor nahlas.
- Fakta o konkrétních blocích ber z docs/generated/INVENTORY.md; ověř, že jeho otisk odpovídá exportu.
- Zachovej přesné názvy bloků, členů DB, UDT a instancí, pokud změna názvu není v zadání.
- Zachovej i existující překlepy ve veřejných symbolech.
- Názvy mohou používat HMI, receptury, logging nebo externí zařízení mimo export.
- Před změnou rozhraní dohledávej všechna volání, instance a známé externí vazby.
- Dodavatelské bloky (podle názvu a hlavičky AUTHOR/FAMILY) považuj za referenci;
  úprava vyžaduje konkrétní zadání a analýzu všech použití.
- Aplikační obal dodavatelského bloku nezaměňuj automaticky s dodavatelskou knihovnou.
- Hromadný přepis nebo přeformátování exportu bez zadání nedělej.
- Sdílené typy a globální DB vyžadují kontrolu všech linek a stanic, kterých se změna týká.
- Bez zadání neměň HW_ID, telegramy, TO konfiguraci, pohybové limity ani retenci.
- Diagnostické symboly se slovy Safety a Emergency nejsou dokladem certifikované safety funkce.
- Nezasahuj do bezpečnostní funkce ani neobcházej blokování v rámci běžného refaktoringu.
- Nespouštěj download do fyzického PLC ani online změny jako součást tvorby zdroje.
- Nezapisuj projektový kód mimo deklarovaný workspace, drafts/ a dokumentaci.
- Zjištěné závady mimo zadání uveď jako nález s důkazem a dopadem.
