#include "FooLista.hpp"

FooLista::FooLista():head(nullptr){}   
FooLista::FooLista(const FooLista& other) {
  *this=other; // meh, lustasag fel egeszseg
}
FooLista::~FooLista(){
  Elem* tmp;
  while(head!=nullptr) {
    tmp=head;
    head=head->next;
    delete tmp;
  }     
}
FooLista& FooLista::operator=(const FooLista& other) {
  head=nullptr;
  for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
    addFoo(tmp->adat); // forditott sorrend
  return *this;
}
void FooLista::addFoo(const Foo& t){
  Elem* tmp=new Elem;
  tmp->adat=t;
  tmp->next=head;
  head=tmp;
}
bool FooLista::hasFoo(const Foo& t) const {      
  for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
    if(tmp->adat == t)
      return true;
  }
  return false;
}


Foo& FooLista::getFoo(const Foo& t){
  for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
    if(tmp->adat == t)
      return tmp->adat;
  }
  // TODO throw exception
}

std::ostream& operator<<(std::ostream& s, const FooLista& tl){
  for(FooLista::Elem* tmp=tl.head; tmp!=nullptr; tmp = tmp->next) {
    s <<"  - "<< tmp->adat<<std::endl;
  }
  return s;
}
