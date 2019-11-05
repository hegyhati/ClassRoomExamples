#include <iostream>
#include <string>
using namespace std;

struct LLItem{
  int data;
  LLItem* next;
};

void push_back(LLItem*& head, int newData){
  if(head==nullptr){
    head  = new LLItem;
    head->data = newData;
    head->next = nullptr;
    //cerr << "pushed " << newData <<" to LLItem at "<< head << endl;
  } else {
    LLItem* tmp=head;
    while(tmp->next!= nullptr) tmp=tmp->next;
    tmp->next = new LLItem;
    tmp->next->data = newData;
    tmp->next->next = nullptr;
    //cerr << "pushed " << newData <<" to LLItem at "<< tmp->next << endl;
  }
}

void print(LLItem* head){\
  //cerr << "Printing out data stored at LLItem at "<< head << endl;
  if(head!=nullptr) {
    cout << head->data << " --- ";
    print(head->next);
  }
}

void print2(LLItem* head){
  for(LLItem* tmp=head; tmp!= nullptr; tmp=tmp->next)   
    cout << tmp->data << " --- ";
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
  int number;
  do{
    cin >> number;
    if(number!=0) push_back(head,number);
  } while (number!=0);

  print(head);
  cout << endl;
  print2(head);
  cout << endl;

  erase(head);

  return 0;
}
