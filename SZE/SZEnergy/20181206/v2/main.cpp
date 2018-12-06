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



class HallgatoLista {
    struct Elem {
        Hallgato adat;
        Elem* next;
    };
  
    Elem* head;
  public:
    HallgatoLista():head(nullptr){}   
    HallgatoLista(const HallgatoLista& other) {
      *this=other; // meh, lustasag fel egeszseg
    }
    ~HallgatoLista(){
      Elem* tmp;
      while(head!=nullptr) {
        tmp=head;
        head=head->next;
        delete tmp;
      }     
    }
    HallgatoLista& operator=(const HallgatoLista& other) {
      head=nullptr;
      for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
        addHallgato(tmp->adat); // forditott sorrend
      return *this;
    }
    void addHallgato(const Hallgato& h){
      Elem* tmp=new Elem;
      tmp->adat=h;
      tmp->next=head;
      head=tmp;
    }
    bool hasHallgato(const Hallgato& h) const {      
      for(Elem* tmp=head;tmp!=nullptr;
        tmp = tmp->next) {
        if(tmp->adat.getNeptun() == h.getNeptun())
          return true;
      }
      return false;
    } 
};

class Targy{
    string nev;
    string neptun;
    int kredit;
    // elofeltetelek
    HallgatoLista hallgatok;
    
  public:
    Targy(string nev="", string neptun="", int kredit=0)
      :nev(nev),neptun(neptun),kredit(kredit) {}
      
    string getNev() const { return nev; }
    string getNeptun() const { return neptun; }
    
    void addHallgato(Hallgato h) {
      hallgatok.addHallgato(h);
    }
    
    bool hasHallgato(Hallgato h) const {      
      return hallgatok.hasHallgato(h);
    } 
    
};




class TargyLista {
    struct Elem {
        Targy adat;
        Elem* next;
    };
  
    Elem* head;
  public:
    TargyLista():head(nullptr){}   
    TargyLista(const TargyLista& other) {
      *this=other; // meh, lustasag fel egeszseg
    }
    ~TargyLista(){
      Elem* tmp;
      while(head!=nullptr) {
        tmp=head;
        head=head->next;
        delete tmp;
      }     
    }
    TargyLista& operator=(const TargyLista& other) {
      head=nullptr;
      for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
        addTargy(tmp->adat); // forditott sorrend
      return *this;
    }
    void addTargy(const Targy& h){
      Elem* tmp=new Elem;
      tmp->adat=h;
      tmp->next=head;
      head=tmp;
    }
    bool hasTargy(const Targy& h) const {      
      for(Elem* tmp=head;tmp!=nullptr;
        tmp = tmp->next) {
        if(tmp->adat.getNeptun() == h.getNeptun())
          return true;
      }
      return false;
    } 
};

class Felev{
    int ev;
    string evszak;
    TargyLista targyak;

  public:
    
    Felev(int ev, string evszak) :ev(ev),evszak(evszak){}
      
    int getEv() const { return ev; }
    string getEvszak() const { return evszak; }
    
    void addTargy(Targy t) {
      targyak.addTargy(t);
    }
    
    bool hasTargy(Targy t) const {      
      return targyak.hasTargy(t);
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
