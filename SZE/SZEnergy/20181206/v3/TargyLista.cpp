#include "TargyLista.hpp"

TargyLista::TargyLista():head(nullptr){}   
TargyLista::TargyLista(const TargyLista& other) {
  *this=other; // meh, lustasag fel egeszseg
}
TargyLista::~TargyLista(){
  Elem* tmp;
  while(head!=nullptr) {
    tmp=head;
    head=head->next;
    delete tmp;
  }     
}
TargyLista& TargyLista::operator=(const TargyLista& other) {
  head=nullptr;
  for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
    addTargy(tmp->adat); // forditott sorrend
  return *this;
}
void TargyLista::addTargy(const Targy& t){
  Elem* tmp=new Elem;
  tmp->adat=t;
  tmp->next=head;
  head=tmp;
}
bool TargyLista::hasTargy(const Targy& t) const {      
  for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
    if(tmp->adat.getNeptun() == t.getNeptun())
      return true;
  }
  return false;
}


Targy& TargyLista::getTargy(const Targy& t){
  for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
    if(tmp->adat.getNeptun() == t.getNeptun())
      return tmp->adat;
  }
  // TODO throw exception
}

std::ostream& operator<<(std::ostream& s, const TargyLista& tl){
  for(TargyLista::Elem* tmp=tl.head; tmp!=nullptr; tmp = tmp->next) {
    s <<"  - "<< tmp->adat<<std::endl;
  }
  return s;
}
