# SCL a kompatibilita

## Konvence
- Projekt může používat více konvencí pojmenování. Při úpravě zachovej konvenci konkrétního modulu.
- Konvence pozorované v projektu jsou v projektových invariantech, ne zde.
- U nového modulu popiš zvolenou konvenci; nenormalizuj související starší bloky.

## Pravidla implementace
- Používej SCL syntaxi a instrukce pro potvrzenou cílovou verzi TIA/CPU.
- Rozhraní instrukcí a knihoven odvozuj ze skutečných deklarací nebo dokumentace dané verze.
- Zachovej atributy exportu, VERSION, deklarace RETAIN/NON_RETAIN, startovní hodnoty a viditelnost.
- Číslo VERSION měň jen podle dohodnuté politiky projektu, ne automaticky při každé editaci.
- Neodstraňuj položky typu "*** ... ***"; jsou skutečnými členy datové struktury.
- VAR_TEMP přiřaď před každým možným čtením; není to paměť předchozího cyklu.
- Stav mezi cykly ukládej do odpovídajících statických dat nebo DB.
- Typ, rozsah a jednotku každé nové veličiny stanov výslovně.
- Převody typů dělej vědomě; kontroluj přetečení, ztrátu přesnosti a znaménko.
- Před indexováním ověř meze pole; před dělením nenulový jmenovatel.
- Používej pojmenované parametry volání v souladu s existujícím blokem.
- U nového kódu preferuj pojmenované konstanty pro významové hodnoty a stavy.
- Smysluplné komentáře popisují důvod, jednotky, handshake a hraniční chování.
- Nepřidávej tvrzení o provedené kompilaci nebo zkoušce, která neproběhla.
- Uprav jen nutné řádky. Zachovej okolní odsazení, zakončení řádků, BOM a kódování.
