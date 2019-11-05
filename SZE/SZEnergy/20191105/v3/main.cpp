#include <iostream>
#include <string>
using namespace std;

class Whatever {
    int foo;
    double bar;
  public:
    Whatever(int foo=0, double bar=0.0): foo(foo), bar(bar){}
    int getFoo() const {return foo;}
    void print() const { cout << " ["<<foo<<","<<bar<<"> "; }
};

struct LLItem{
  Whatever data;
  LLItem* next;
};



class LL {
    LLItem* head;

    void recursive_print(LLItem* current) const {
      if(current!=nullptr) {
        current->data.print();
        cout << " --- ";
        recursive_print(current->next);
      }
    }
  public:
    LL():head(nullptr){}
    
    void push_back(Whatever newData){
      if(head==nullptr){
        head  = new LLItem;
        head->data = newData;
        head->next = nullptr;
      } else {
        LLItem* tmp=head;
        while(tmp->next!= nullptr) tmp=tmp->next;
        tmp->next = new LLItem;
        tmp->next->data = newData;
        tmp->next->next = nullptr;
      }
    }

    void print() const { recursive_print(head); }


    void pop_front(){
      if(head!=nullptr){
        LLItem* tmp=head->next;
        delete head;
        head=tmp;
      }
    }

    void erase() {
      while(head!=nullptr)
        pop_front();
    }
};




int main(){
  LL list;
  int foo; double bar;
  do{
    cin >> foo >> bar;
    if(foo!=0) list.push_back(Whatever(foo,bar));
  } while (foo!=0);

  list.print();
  cout << endl;

  list.erase();

  return 0;
}
