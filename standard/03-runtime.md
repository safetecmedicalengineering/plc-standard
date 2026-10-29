# Cykly PLC, sekvence a zařízení

## Pořadí vykonávání
- Před úpravou zjisti volající OB, periodu, pořadí volání a sdílené proměnné.
- Změna pořadí může posunout reakci o cyklus. Neprováděj ji jako kosmetickou úpravu.
- U sekvenčních automatů rozliš požadovaný a skutečný krok a okamžik volání sekvence.
- Nepřeskakuj mechanismus krokování ani jiné režimy definované standardem stanic projektu.
- U stanic navazuj na existující standard stanic projektu (viz projektové invarianty).
- Nepřidávej druhý konkurenční automat režimů, pokud to nevyžaduje specifikace.
- Odděl automatický režim, jeden cyklus, krokování, seřízení a návrat do základní polohy.
- U sdíleného FB prověř globální přístupy i všechny instance, nejen jeho rozhraní.
- Ověř, že instanční DB patří FB dané linky či stanice; kopie bloků s pevnými globálními odkazy
  (např. na L1) pod cizí instancí ovládají jiné zařízení.

## Paměť a signály
- U každého výstupu nebo sdíleného povelu určuj vlastníka a pravidla zápisu.
- Rozliš úrovňový signál, impuls, hranu, latched stav a acknowledge handshake.
- U timerů a hran popiš četnost volání, držení interního stavu a reset.
- Změnu podmíněného volání na nepodmíněné nebo opačně považuj za změnu chování.
- Při předčasném RETURN prověř zachované výstupy, povely a nepovolané instance.
- Nemazej všechny výstupy automaticky na začátku cyklu bez znalosti jejich kontraktu.

## Přerušení, dávkování a pohyb
- Pro data sdílená mezi OB urči zapisující kontext a způsob konzistentního předání.
- Periodu přerušení, časové jednotky ani synchronizaci neodvozuj z názvu OB ani proměnné;
  ověř je v HW konfiguraci.
- Výstupy vlastněné přerušovacím OB nezapisuj z cyklického OB ani jiného bloku.
- U pohybů ověř jednotky mm/deg, modulo, referenci, polohu, handshake a ukončení povelu.
- HW_ID ani telegram nevybírej podle podobnosti s vedlejší linkou.
- U RUNTIME a čítačů ověř inicializaci, jednotky, reset, přetečení a neplatný vzorek.
- Komentáře o senzorech jsou projektové předpoklady; pro změnu ověř skutečnou konfiguraci.

## Přerušení činnosti a testy
- Specifikuj Stop, odebrání Enable, ztrátu podmínky, timeout, reset a restart PLC.
- Prioritu současných povelů odvozuj ze schválené specifikace.
- Výchozí nebo neplatný stav automatu musí mít popsanou reakci a diagnostiku.
- Ověř, co se obnoví po retentivním restartu a co se inicializuje při prvním volání.
- Minimální scénáře: běžný cyklus, Stop během kroku, timeout, chyba zařízení,
  reset při trvající chybě, opětovný Start a stav po restartu.
- U společné funkce navíc proveď regresní scénáře pro všechny dotčené linky.
