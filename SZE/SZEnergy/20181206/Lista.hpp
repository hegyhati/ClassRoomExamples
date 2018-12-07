#ifndef LISTA_HPP
#define LISTA_HPP

#include <fstream>

template <class Foo>
class Lista;

template <class Foo>
std::ostream& operator<<(std::ostream& s, const Lista<Foo>& tl);

template <class Foo>
class Lista {
    struct Elem {
        Foo adat;
        Elem* next;
    };
  
    Elem* head;
  public:

    Lista():head(nullptr){}   
    Lista(const Lista& other) {
      *this=other; // meh, lustasag fel egeszseg
    }
    ~Lista(){
      Elem* tmp;
      while(head!=nullptr) {
        tmp=head;
        head=head->next;
        delete tmp;
      }     
    }
    Lista& operator=(const Lista& other) {
      head=nullptr;
      for(Elem* tmp=other.head; tmp!=nullptr; tmp=tmp->next)
        add(tmp->adat); // forditott sorrend
      return *this;
    }
    void add(const Foo& t){
      Elem* tmp=new Elem;
      tmp->adat=t;
      tmp->next=head;
      head=tmp;
    }
    bool has(const Foo& t) const {      
      for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
        if(tmp->adat == t)
          return true;
      }
      return false;
    }


    Foo& get(const Foo& t){
      for(Elem* tmp=head; tmp!=nullptr; tmp = tmp->next) {
        if(tmp->adat == t)
          return tmp->adat;
      }
      // TODO throw exception
    }

    friend std::ostream& operator<< <Foo>(std::ostream& s, const Lista<Foo>& tl);
};



template <class Foo>
std::ostream& operator<<(std::ostream& s, const Lista<Foo>& tl){
  for(typename Lista<Foo>::Elem *tmp=tl.head; tmp!=nullptr; tmp = tmp->next) {
    s <<"  - "<< tmp->adat<<std::endl;
  }
  return s;
}




#endif
