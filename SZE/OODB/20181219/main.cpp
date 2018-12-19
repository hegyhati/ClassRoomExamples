/*
 * Elégséges szint:
 *
 *
 * Egy fájlrendszer működését "modellezzük" a programunkkal.
 *
 * Készítsen egy File osztályt, melynek két adattagja van: a neve és a tartalma.
 * Mindkettő tetszőleges karaktersorozat, konstruktorban a név kötelező, a tartalom alapértelmezetten üres sztring. Az adattagokat kívülről csak olvasni lehessen.
 *
 * Készítsen egy Directory osztályt, mely fájlokat tud tárolni, azokból tetszőleges számút. (Alkönyvtárakat egyelőre nem.)
 * Egy Directory-t a nevének megadásával tudunk létrehozni.
 * 
 * A Directory osztálynak legyen egy touch függvénye, mely paraméterként vár egy fájlnevet és opcionálisan egy tartalmat.
 * Ha az adott fájlnévvel még nincs fájl a könyvtárban, akkor hozza létre a megadott tartalommal, és térjen vissza 0-val. 
 * Ha van már ilyen nevű file, akkor ne csináljon semmit, és térjen vissza 1-gyel.
 *
 * A Directory osztálynak legyen egy ls függvénye, mely kilistázza a benne levő fájlokat.
 *
 * Készítsen egy Filesystem osztályt, mely egy olyan fájlrendszert modellez, ahol a "gyökérben" vannak fájlok és könyvtárak.
 * Legyen az osztálynak egy mkdir függvénye, mely megadott névvel megpróbál létrehozni egy könyvtárat. Ha már létezik, akkor térjen vissza 1-gyel, különben 0-val.
 * Legyen egy touchindir függvénye az osztálynak, mely első paraméterként egy fájlnevet vár, második paraméterként az opcionális tartalmat, harmadik paraméterként pedig opcionálisan egy könyvtárnevet.
 * Ha a harmadik paraméter nincs megadva, akkor a gyökérbe, ha meg van adva, akkor a megadott könyvtárba próbálja létrehozni a fájlt.
 * A függvény térjen vissza 0-val, ha a művelet sikeres volt, 1-gyel, ha a fájl már létezik, és 2-vel, ha a harmadik paraméterben megadott könyvtár nem létezik. (Ez esetben ne is hozza létre.)
 *
 * Végezetül legyen egy treelist függvény, mely "fa nézetben" kiírja a fájlrendszer tartalmát. Pl az alábbi main függvény végén ezt:
 *
 * /
 *  Kozmondasok/
 *    Kut.txt  
 *  Idezetek/
 *    Gandalf.txt
 *    Samuel.txt  
 *  Readme.md
 *
 *
 * Feladatok plusz pontokért
 *
 * A Directory könyvtárban lehessenek könyvtárak is, és legyen meg neki is az mkdir függvénye.
 *
 * Ha az előző már megvan, legyen a Filesystem-nek egy cd függvénye, mellyel beléphetünk egy könyvtárba, és ott adhatunk ki touch/mkdir/ls parancsokat. A cd("..") parancs hatására lépjen ki a szülő könyvtárba, ha pedig a gyökérben vagyunk, akkor ne csináljon semmit, és térjen vissza 1-el. (Akkor is 1-gyel térjen vissza, ha nincs ilyen nevű könyvtár, minden más esetben 0-val.)
 *
 * Legyen a FileSystem osztálynak egy pwd függvénye, mely visszaadja, hogy hol vagyunk, pl: "/Idezetek/GyurukUra/KetTorony/"
 *
 * A touch és mkdir függvények működjenek abszolút és relatív path-okkal is, pl ha:
 * .pwd();  => /Idezetek/
 * akkor a következő két parancs legyen ekvivalens:
 * .touch("/Idezetek/Gyurukura/Smeagol.txt", "My precious");
 * .touch("Gyurukura/Smeagol.txt", "My precious");
 * (A touch-nak nincs harmadik parametere)
 *
 * Legyen egy LinkFile származtatva a File osztályból, melynek a tartalma egy másik fájl elérési útja.
 * ln(mi,mire) függvénnyel lehessen egy már meglévő fájlra, vagy linkre beállítani egy link fájlt. (A mi/mire abszolút, vagy relatív útvonalak. Hibakódok a fentiekhez hasonlóan.)
 * cat(fájlnévelérésiúttal) függvénnyel lehessen kiiratni egy fájl tartalmát, ha pedig link, akkor a mutatott fájl tartalmát írja ki. (Ha nem létezik, akkor egy error üzenetet.)
 *
 * Készítsen egy commandline osztályt, melynek egyetlen run függvénye van, mely egy megszokott terminált emulál. Prompt, amiben lehet használni a fenti parancsokat (cd/mkdir/touch/ls/...) a megszokott módon.
 */


#include <iostream>
using namespace std;

#include "Filesystem.h"
#include "Directory.h"
#include "File.h"


int main(){

  Filesystem foo;
  foo.mkdir("Idezetek");
  foo.mkdir("Kozmondasok");
  foo.touchindir("Readme.md","Az Idezetek konyvtartban idezetek vannak, a Kozmondasok konyvtarban kozmondasok. dah....\n");
  foo.touchindir("Kut.txt","Addig jar a korso a kutra, amig el nem torik.","Kozmondasok");
  foo.touchindir("Gandalf.txt","Fussatok bolondok!","Idezetek");
  foo.touchindir("Samuel.txt","I dare you, I double dare you!","Idezetek");
  foo.treelist();
  
}
