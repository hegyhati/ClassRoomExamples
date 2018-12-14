/*
 Könyvnyilvántartó program

 Készítsen C++ osztályokat könyvek adatainak tárolására, az alábbi specifikációk alapján!

 Készítsen egy Konyv osztályt egy könyv adatainak tárolására: cím, szerző, kiadás éve.
 Az adatokat ne lehessen az osztályon kívülről módosítani, csak getter függvényekkel lekérdezni.

 Készítsen egy Kotet osztályt, ami a Konyv osztályból származik, és hozzáfér annak adattagjaihoz, valamint két további adattagja van: sorozat neve, és kötetszám.

 A Konyv és Kotet osztályoknak ne legyen paraméter nélküli konstruktora, csak az összes adattag inicializálásával lehessen őket létrehozni.

 Készítsen egy Konyvtar osztályt, ami Konyv és Kotet objektumokat képes tárolni.
 Legyen képes előre ismeretlen számú könyvet és sorozatot eltárolni.
 A Konyvtar osztálynak legyen egy add() függvénye, ami egy Konyv pointert vár, és beilleszti a listába.
 A Konyvtar destruktora szabadítsa fel a könyveknek és sorozatoknak lefoglalt memóriát.
 
 A Konyvtar-nak legyen egy print függvénye, mely kilistázza az összes könyvet, kötetet. A Konyv adatai a következő formában jelenjenek meg: "[Szerző] - [Cím] ([Év])", a Kotet adatai pedig "[Sorozatcím]/[Kötet sorszáma]: [Szerző] - [Cím] ([Év])" ([]-ek nélkül).

 ---- elégséges szint határa ----

 A Konyvtar-nak legyen egy db(string szerzo, string cim) függvénye, mely megadja, hogy egy adott szerzőtől egy adott című könyv/kötet hányszor van meg. (A kiadás éve irreleváns.)

 Mindegyik osztályt lehessen << operátorral ostream objektumra "küldeni" a fent leírt formai megkötések mellett.

 A Konyvtar osztalynak legyen [int idx] operátora, mely visszaad egy nem módosítható pointert az idx-edik elemre, ha az létezik, egyébként nullptr-t.

 A Konyvtar-nak legyen egy rendez() függvénye, mely a könyveket szerző, majd cím szerinti ABC sorrendbe rendezi.

 A Konyvtar-nak legyen egy [string sorozatcim] operátora, mely list<const Konyv*> formában visszaadja az ahhoz a sorozathoz tartozó könyvek listáját.

 
*/

#include "Konyvtar.h"
#include "Konyv.h"
#include "Kotet.h"

int main(){

  /* Kettes szint tesztelese */
  Konyvtar sajat;
  sajat.add(new Kotet("J. K. Rowling", "Harry Potter es az azkabani fogoly",2009,"Harry Potter",5));
  sajat.add(new Konyv("Fekete Istvan","Vuk",1993));
  sajat.add(new Kotet("J. K. Rowling", "Harry Potter es a titkok kamraja",2003,"Harry Potter",2));
  sajat.add(new Kotet("J. K. Rowling", "Harry Potter es a bolcsek kove",2002,"Harry Potter",1));
  sajat.add(new Konyv("Fekete Istvan","Vuk",1993));

  sajat.print();

  /* Tovabbi feladatok tesztelese */

  
  std::cout<<"\n\nKonyvtar::db(string)\n";
  std::cout<<    "--------------------\n";
  std::cout<<"A Vuk "<<sajat.db("Fekete Istvan","Vuk")<<" peldanyban van meg\n";

  
  std::cout<<"\n\nostream& << Konyv/Kotet\n";
  std::cout<<    "-----------------------\n";
  std::cout<<Konyv("J. R. R. Tolkien","Szilmarillok",1986)<<std::endl;
  std::cout<<Kotet("Raymond E. Feist","Magus a mester",2003,"Reshaboru",3)<<std::endl;
  
  std::cout<<"\n\nKonyvtar::operator[] (unsigned int)\n";
  std::cout<<    "-----------------------------------\n";
  for(unsigned int i=0;i<1000;i++){
    if(sajat[i]!=nullptr)
      std::cout<<"Az "<<i+1<<". konyvem: "<<sajat[i]->toString()<<std::endl;
    else
      break;
  }
  
  std::cout<<"\n\nKonyvtar::rendez()\n";
  std::cout<<    "------------------\n";
  sajat.rendez();
  sajat.print();
  
  std::cout<<"\n\nKonyvtar::operator[](string)\n";
  std::cout<<    "----------------------------\n";
  std::cout<<"A Harry Potter sorozatbol megvan:\n";
  for(auto k:sajat["Harry Potter"])
    std::cout<<" - "<<*k<<std::endl;

  
  
  
  return 0;
  
}
