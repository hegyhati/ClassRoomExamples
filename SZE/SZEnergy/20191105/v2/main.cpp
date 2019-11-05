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

void push_back(LLItem*& head, Whatever newData){
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

void print(LLItem* head){\
  if(head!=nullptr) {
    head->data.print();
    cout << " --- ";
    print(head->next);
  }
}

void print2(LLItem* head){
  for(LLItem* tmp=head; tmp!= nullptr; tmp=tmp->next)  {
    head->data.print();
    cout << " --- ";
  }
}

void erase (LLItem*& head){
  if (head != nullptr){
    erase (head->next);
    delete head;
    head = nullptr;
  }
}

void pop_front(LLItem*& head){
  if(head!=nullptr){
    LLItem* tmp=head->next;
    delete head;
    head=tmp;
  }
}

void erase2(LLItem*& head) {
  while(head!=nullptr)
    pop_front(head);
}

int main(){
  LLItem* head = nullptr;
  int foo; double bar;
  do{
    cin >> foo >> bar;
    if(foo!=0) push_back(head,Whatever(foo,bar));
  } while (foo!=0);

  print(head);
  cout << endl;
  print2(head);
  cout << endl;

  erase(head);

  return 0;
}
