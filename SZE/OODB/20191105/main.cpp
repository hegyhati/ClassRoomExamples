/*

A ZH-val kapcsolatos altalanos informaciok:

Szigoru elvarasok:
 - Ez a main.cpp nem modosithato azon kivul, hogy kikommentezed azt, amit nem akarsz (meg) futtatni. Pl plusz jegyeket tesztelo kod, vagy felkesz program eseten akar az alapokat tesztelo kod.
 - A sajat tesztjeidet ne ide, hanem a main elso soraban meghivott myTest() fuggvenybe tedd epp ezert menetkozben, amelyet a MyTest.cpp-ben irogass meg.
 - Forditasi hiba, memoriaszemeteles, segfault, stb. automatikus elegtelent jelent. (Figyelj kulonosen a copy konstruktorokra, destruktorokra, stb.)
 - Az osztalyok mukodesere annyi megkotes van, ami a leirasban adott, illetve a teszter fuggvenyben levokbol adodik. 
 - Header guardok legyenek rendben.
 - Ha dobalsz exception-t, kapd is el.
 - NE hasznalj platformfuggo dolgokat, csak standard C++-t, es NE allitsd meg a program futasat a vegen egy beolvasassal.
 - C++11-es dolgokat hasznalj batran. Ha kesobbi dolgokra epitkeznel, azt jelezd valahogy.
 - Az altalad irt kodban (a pluszpontos fajlbeolvasason kivul) semmilyen I/O muvelet ne legyen. 

Kevesbe egzakt, de fontos iranymutatasok:
 - Ami lehet const (argumentumok, metodusok, adattagok), azt legyen is az. Ha 1 ilyen lemarad, nem baj, de ha sok helyen hianyzik, az sulyos hiba.
 - Keruld a redundans kodot. Ha valamilyen logikad ket helyen is megvan, akkor szervezd ki fuggvenybe, ososztalyba, csinalj belole template-et, hasznalj alapertelmezett argumentum ertekeket, stb. Talald meg ra az idealis eszkozt. 
 - Amit lehet konstruktor inicializalo listajaban beallitani, azt ne a fuggvenytorzsben allitsd be.
 - Indentald ertelmesen a kododat.
 - A sajat osztalyaidban ne hasznald a using namespace-t, a myTest fuggvenyben nyugodtan.
 - Ha valamire van nagyon alap std eszkoz, probald meg hasznalni ahelyett hogy feltalalod a melegvizet.

Jotanacsok:
 - A billentyuzet pufolese elott gondold at, mit akarsz, hogyan megcsinalni, firkalj, epitsd fel a programod szerkezetet.
 - Tesztelj gyakran, epitkezz inkrementalisan. 
 - Ne bonyolitsd tul a dolgokat.
 - Elsore mukodjon jol, ugy ahogy megtervezted, es ha kell, utana szepitsd. Inkabb legyen csunya, de jo, mint kacsalabon forgo, de rossz.
 - Emberbol vagyunk, hibazhatunk a zh kiirasban. Ha valahol ugy erzed, nem stimmel valami, tedd fel a kezed, es kerdezz. 
 - Ha valamit nem vagy biztos, hogy jol erted-e, inkabb kerdezd meg, minthogy rosszul ertelmezed, es 1 ora kodolas utan kiderul, hogy dobhatsz mindent a kukaba. 
 - Ne copy paste-elj olyan kodot, amirol csak kb tudod, mit csinal. Ha mindent kezzel potyogsz be, semmi auto kiegeszitest nem hasznalsz, akkor is eleg rovid a kod ahhoz, hogy beleferjen az idodbe. 
 - Ne irj meg olyan fuggvenyeket, amiket ugysem fogsz hasznalni. (lasd tervezesi szakasz.)
 - Eleinte irj placeholder fuggvenytorzseket, hogy minel hamarabb tudd a kodod reszleteit tesztelni.

 
Es akkor a feladat:

Keszits egy MonthlyPhoneLog osztalyt, ami tarolja, hogy egy honapban hany perc volt a kimeno hivasod, es hany sms-t kuldtel el. (Egyelore nem szamit, hogy halozaton belul, kivul, roaming, stb.)

Legyen tovabba egy absztrakt Tariff osztaly, aminek (egyelore) egyetlen fuggvenye van: calculateBill, ami kap egy MonthlyPhoneLog referenciat, es kiszamolja, hogy azzal a tarifaval mennyi lett volna a havi szamla.

Szarmaztass ebbol az osztalybol egy olyat, hogy SimpleTariff, aminek van egy percdija, meg egy sms dija, illetve hogy mennyi a szamlazasi alaptetel hivashossz tekinteteben (masodpercenkent, percenkent, lasd main, alapertelmezetten masodpercenkent).

Szarmaztass a Tariff-bol egy FixBaseTariff-ot, aminel meg van adva egy lebeszelheto (sms nem) alaposszeg, amit mindenkeppen befizetunk, illetve hogy ennek a keretnek az erejeig mekkora a percdij, utana mennyi a percdij, valamint mennyi az sms ara. 

Plusz jegyekert feladatok:
 - MonthlyPhoneLog osztalybol szarmazzon egy RealMonthlyPhoneLog, ami egy fajlbol olvassa be hivasoknak, sms-eknek a listajat. A fajlban tetszoleges formatumban minden hivasrol szerepel hogy ki volt a hivott fel, mikor kezdodott a hivas, mennyi ideig tartott. SMS-rol pedig, hogy ki volt a cimzett, mikor, es hany db SMS-be fert bele az uzenet.
 - A Tariffbol, vagy valamely gyerekebol (amelyikbol a legcelszerubb), szarmazzon egy PrePaid osztaly, ami a feltoltokartyanak felel meg. Adott, hogy mennyi a keret, a percdij, az sms, es hogy milyen alapu a szamlazas. Ha egy havi hivaslista nem fer bele a keretbe, akkor dobjon egy NotEnoughCredit exceptiont.
 - Egeszitsd ki a meglevo osztalyokat ugy, hogy legyen kulonbseg a halozaton beluli es a halozaton kivuli kommunikacio dijszabasaval. Mindezt azonban ugy, hogy visszafele kompatibilis maradjon a kod.
 
 */
 
#include <iostream>
#include <map>
#include <string>
#include "MonthlyPhoneLog.hpp"
//#include "RealMonthlyPhoneLog.hpp"
#include "Tariff.hpp"
#include "SimpleTariff.hpp"
#include "FixBasedTariff.hpp"
//#include "PrePaid.hpp"

void myTest();

void testEssential(){
  const MonthlyPhoneLog january(1234 /* s */, 56 /* SMS */);
  std::map< std::string, const Tariff*> options;
  options["Simple, second based"] = new SimpleTariff(30 /* HUF/min */, 20 /* HUF/SMS */); 
  options["Simple, minute based"] = new SimpleTariff(25 /* HUF/min */, 20 /* HUF/SMS */, 60 /* s */);
  options["FixBase-1000"] = new  FixBasedTariff(1000 /* HUF */, 20 /* HUF/min */, 30 /* HUF/min */, 20/* HUF/SMS */);   
  options["FixBase-2000"] = new  FixBasedTariff(2000 /* HUF */, 15 /* HUF/min */, 25 /* HUF/min */, 15/* HUF/SMS */);
  
  std::cout<<"January would cost me:"<<std::endl;
  for (const auto& option: options) {
    std::cout << " - " << option.second->calculateBill(january) << " HUF with " << option.first << std::endl;
    delete option.second;
  }
}

void testPlusRealLog() { }
void testPlusPrePaid() { }
void testPlusNetworkBased() { }

int main(){
  myTest();
  testEssential();
  testPlusRealLog();
  testPlusPrePaid();
  testPlusNetworkBased();
}


