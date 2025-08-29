# Projektfeladat, cél

## Indíttatás

A szakmai közéletben sokszor találkozhatunk vitákkal azzal kapcsolatban, hogy mi is az *igazi OO*, miért terjedt el ilyen mértékben, vagy hogy egyáltalán manapság követendő irány-e még.
Tekintettel arra, hogy a szoftverfejlesztés nem egy egzakt tudomány, hanem egy szakma, sok esetben az egyetlen magabiztosan kijelenthető állítás, hogy ezek a kérdések nem fekete-fehérek, és mindkét oldalon akadnak megfontolásra érdemes érvek, gondolatok. 
Jelen jegyzetnek éppen ezért nem is célja *igazságot tenni*, inkább csak plusz tudást, szempontokat átadni, melyek alapján az olvasó megalapozottabban tud véleményt formálni az adott szituációban.

Bár a fenti kérdések megosztják a szakmai közösséget, vannak pontok, melyekben általánosnak mondható az egyetértés. 
Az objektumorientált paradigmát aktívan kritizálók sem vitatják, hogy rosszabb szoftverfejlesztővé válna valaki attól, hogy ismeri azt, illetve a mögötte levő motivációt, kiváltó okokat, mégha arra más megoldást is lát megfelelőbbnek.
Az OO paradigma térnyerését illetően is egyetértés van abban, hogy születtekor megoldást nyújtott egy olyan problémára, melybe az akkor elterjedt procedurális módszernek beletört a bicskája. 

Ez a probléma pedig nem más, mint az egyre növekvő méretű kódbázisok kezelhető szinten tartása. 

Megfordítva a dolgot: az OO elvek nem néhány száz vagy ezer soros hobbiprojektekre lettek elsősorban kitalálva, értelmük is sokszor lényegesen nagyobb kódbázisok esetén válik nyilvánvalóvá. 
Egy OO jegyzet esetében állandó kihívást jelent, hogy a mutatott példák emészthető méretűek legyenek, ugyanakkor ne tűnjön önkényes modorosságnak, túlzásnak bizonyos eszközök, módszerek, minták használata. 

Jelen jegyzetben ezzel a kihívással a következő módon igyekszünk megbirkózni:
 
  - Egyes fejezetekben új OO fogalmaknak, valamint azok Java nyelven történő megvalósításának ismertetése a cél, kisebb átláthatóbb példákkal illusztrálva. 
  - Minden ilyen fejezetet követően egy *projektfejezet* alkalmazza ezeket az új technikákat, elveket egy nagyobb, és egyre bővülő kódbázison. 

A *projektfejezetek* sok esetben a következő, új tudást átadó fejezet számára is alapot adnak, azaz felvetnek olyan szituációkat, melyek megoldásához az addig ismert eszközök kevesek, vagy legalábbis körülményesek.
Bízunk benne, hogy ezzel a módszerrel a káposzta is megmarad, és a kecske is jóllakik.  

## A konkrét feladat

Bár kétségkívül sok OO elvet kiválóan meg lehetne mutatni mondjuk egy táblázatkezelő alkalmazás építésén, talán izgalmasabb témát jelent egy játék fejlesztése.
A választásunk egyfajta körökre osztott RPG (role-playing game) játék készítésére esett.
A játékunk fejlesztése során azt a valós szoftverfejlesztésben gyakori jelenséget is szimulálni szeretnénk, hogy gyakran nem ismertek teljes mértékben az elkészítendő szoftverrel szemben támasztott követelmények, vagy idővel változnak. 
Ezért most inkább csak ötleteket, fő irányokat sorolunk fel, amik természetes módon alakulnak majd a fejlesztés során. 

> [!NOTE]  
> Sok esetben a funkcionalitások jelentős része már előre jól ismert, ilyenkor az iteratív fejlesztés helyett mindenképpen érdemes egy jól átgondolt tervezési fázis, melyhez a fontosabb elveket, technikákat későbbi fejezetek mutatnak be. 

Pontokba szedve néhány alapötlet:
 - Van egy világ, ahol a karakterünkkel, hősünkkel csatákat kell megvívnunk az ott lévő szörnyek ellen.
 - A hősünknek vannak szokásos alapadatai (támadás, életpont, stb.), valamint képes fejlődni, szintet lépni, ezzel javítva a képességeit.
 - A hős tud tárgyakat felvenni, melyek segíthetnek támadásban, védekezésben, stb.
 - A tárgyak származhatnak dobozokból, legyőzött szörnyektől, vagy boltból.
 - Természetesen a játék állapotát el kell tudni menteni, később betölteni. 


Bátorítunk minden olvasót arra, hogy saját ízlésének megfelelően bővítse az igényeket, funkciókat, majd azoknak a implementációját tervezze meg, az itt közzétett kódokat forkolja le, és bővítse az ötleteinek megfelelően.
