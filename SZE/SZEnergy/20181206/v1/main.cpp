#include <iostream>
#include <string>
using namespace std;

class Hallgato{
    string nev;
    string neptun;
  public:
    Hallgato(string nev="", string neptun="")
      :nev(nev),neptun(neptun) {}
    string getNev() const { return nev; }
    string getNeptun() const { return neptun; }
};

struct HallgatoListaElem {
    Hallgato adat;
    HallgatoListaElem* next;
};

class Targy{
    string nev;
    string neptun;
    int kredit;
    // elofeltetelek
    HallgatoListaElem* hallgatok;
    
  public:
    Targy(string nev="", string neptun="", int kredit=0)
      :nev(nev),neptun(neptun),kredit(kredit), hallgatok(nullptr) {}
    ~Targy(){
      HallgatoListaElem* tmp;
      while(hallgatok!=nullptr) {
        tmp=hallgatok;
        hallgatok=hallgatok->next;
        delete tmp;
      }     
    }
    Targy(const Targy& other) {
      *this=other; // meh, lustasag fel egeszseg
    }

    Targy& operator=(const Targy& other) {
      nev=other.nev;
      neptun=other.neptun;
      kredit=other.kredit;
      hallgatok=nullptr;
      for(HallgatoListaElem* tmp=other.hallgatok; tmp!=nullptr; tmp=tmp->next)
        addHallgato(tmp->adat); // forditott sorrend
      return *this;
    }
      
    string getNev() const { return nev; }
    string getNeptun() const { return neptun; }
    
    void addHallgato(Hallgato h) {
      HallgatoListaElem* tmp=new HallgatoListaElem;
      tmp->adat=h;
      tmp->next=hallgatok;
      hallgatok=tmp;
    }
    
    bool hasHallgato(Hallgato h) const {      
      for(HallgatoListaElem* tmp=hallgatok;tmp!=nullptr;
        tmp = tmp->next) {
        if(tmp->adat.getNeptun() == h.getNeptun())
          return true;
      }
      return false;
    } 
    
};


struct TargyListaElem {
    Targy adat;
    TargyListaElem* next;
};

class Felev{
    int ev;
    string evszak;
    TargyListaElem* targyak;

  public:
    
    Felev(int ev, string evszak)
      :ev(ev),evszak(evszak),targyak(nullptr) {}
    ~Felev(){
      TargyListaElem* tmp;
      while(targyak!=nullptr) {
        tmp=targyak;
        targyak=targyak->next;
        delete tmp;
      }     
    }//TODO operator=, Felev(const Felev&)
      
    int getEv() const { return ev; }
    string getEvszak() const { return evszak; }
    
    void addTargy(Targy t) {
      TargyListaElem* tmp=new TargyListaElem;
      tmp->adat=t; 
      tmp->next=targyak;
      targyak=tmp;
    }
    
    bool hasTargy(Targy h) const {      
      for(TargyListaElem* tmp=targyak;tmp!=nullptr;
        tmp = tmp->next) {
        if(tmp->adat.getNeptun() == h.getNeptun())
          return true;
      }
      return false;
    }    
};

int main(){
  Hallgato Jani("Hollosi Janos","ABC123");
  Hallgato Erno("Horvath Erno", "XYZ987");
  Hallgato Jozsi("Szabo Jozsef", "AAA000");

  Targy CppProg("C++","GIVK-32165",4);

  CppProg.addHallgato(Jani);
  CppProg.addHallgato(Erno);

  cout <<"C++"<<endl;
  cout<<"Jani? "<< ( CppProg.hasHallgato(Jani)?"felvette":"nem vette fel")<<endl;
  cout<<"Erno? "<< ( CppProg.hasHallgato(Erno)?"felvette":"nem vette fel")<<endl;
  cout<<"Jozsi? "<< ( CppProg.hasHallgato(Jozsi)?"felvette":"nem vette fel")<<endl;

  Targy Python("Python","GIVK-32765",2);

  Python.addHallgato(Jozsi);
  cout <<"Python"<<endl;
  cout<<"Jani? "<< ( Python.hasHallgato(Jani)?"felvette":"nem vette fel")<<endl;
  cout<<"Erno? "<< ( Python.hasHallgato(Erno)?"felvette":"nem vette fel")<<endl;
  cout<<"Jozsi? "<< ( Python.hasHallgato(Jozsi)?"felvette":"nem vette fel")<<endl;


  Felev aktualis(2018,"osz");
  aktualis.addTargy(CppProg);
  aktualis.addTargy(Python);

  
  return 0;
}
