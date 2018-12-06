#include "HallgatoLista.hpp"


HallgatoLista::HallgatoLista():head(nullptr){}

HallgatoLista::HallgatoLista(const HallgatoLista& other) {
  *this=other; // meh, lustasag fel egeszseg
}
HallgatoLista::~HallgatoLista(){
  Elem* tmp;
  while(head!=nullptr) {
    tmp=head;
    head=head->next;
    delete tmp;
  }     
}
HallgatoLista& HallgatoLista::operator=(const HallgatoLista& other) {
  head=nullptr;
  for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
    addHallgato(tmp->adat); // forditott sorrend
  return *this;
}


void HallgatoLista::addHallgato(const Hallgato& h){
  Elem* tmp=new Elem;
  tmp->adat=h;
  tmp->next=head;
  head=tmp;
}
bool HallgatoLista::hasHallgato(const Hallgato& h) const {      
  for(Elem* tmp=head;tmp!=nullptr;
    tmp = tmp->next) {
    if(tmp->adat.getNeptun() == h.getNeptun())
      return true;
  }
  return false;
} 
