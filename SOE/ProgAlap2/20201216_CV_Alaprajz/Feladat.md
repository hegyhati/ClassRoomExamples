# CV vizsgafeladat Programozás Alapjai 2 tárgyhoz
Az elkészítendő program áll egy alap részből, melynek maradéktalan teljesítése szükséges az elégséges jegy megszerzéséhez.
Ezen felül adottak plusz feladatok, melyek teljesítésével jobb érdemjegy érhető el.

## Elégséges szint

### 1. lépés: alaposztály
Készítsünk egy `Szoba` osztályt, mely egy alaprajzon egy szobát modellez. Ennek van szélessége és magassága.
 - Legyen az osztályhoz egy kétparaméteres konstruktor, mely ezeket megadja.
 - Legyen egy `falhossz` függvénye, mely visszaadja, hogy milyen hosszu fal veszi körbe.
 - Legyen egy `alapterulet` függvénye, mely visszaadja az alapterületét.


### 2. lépés: Alaprajz

Legyen egy `Telek` osztályunk, melynek szintén van szélessége és hosszúsága, amit konstruktorban megkap. Ez reprezentálja a telket, amire szobákat építhetünk rá.
  - Legyen egy `raepit` függvénye, mely paraméterként kap egy szobát, valamint azt, hogy a teleken belül hova szeretnénk felépíteni a szobát (x,y koordináták.). A függvény felépíti / leteszi a szobát, hogyha nem fed át semmelyik korábban letett szobával. Ha igen, akkor dobjon egy kivételt. (FOKSZ-osoknak legyen `bool` visszatérési értéke, mely a sikerességet indikálja.)
  - Legyen egy `beepitettseg` függvénye, mely megadja, hogy a telek hány százaléka lett beépítve 
  - Legyen egy `kirajzol` függvénye, mely kirajzolja a telket a következő módon: minden karakter egy 1x1 méteres területet jelöl. Ha ezen a területre belóg legalább egy szoba, akkor `██` legyen kiírva, különben `░░`.

 
## Feladatok plusz jegyért
 - A `kirajzol` függvény legyen paraméterezhető, hogy egy karakter egy hányszor hányas négyzet alakú területet jelöl.
 - Legyen egy `teljesfalhossz` függvény, ami megadja, hogy mennyi a teljes falhossz. Két szoba ha szomszédos, akkor a közös falrészt csak egyszer kell számolni.
 - Grafikus felület vizualizáláshoz, ahol új szobák adhatók hozzá a telekhez, és egy jelölő pirosra vált, ha a beépítettség elér egy megadott százalékot.
 - Lehessen ráépíteni emeletet egy területre, ha az teljesen le van fedve már szobákkal.
