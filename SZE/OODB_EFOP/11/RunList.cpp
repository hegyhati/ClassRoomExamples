#include "RunList.hpp"
#include <fstream>

RunList::~RunList(){
  for(RunListElement *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head->data;
    delete head;    
  }
}

void RunList::add(Run* prun)
{
  if (head==nullptr) {
    head = new RunListElement;
    head ->data=prun;
    head ->next=nullptr;
  } else {
    RunListElement *tmp=head;
    while(tmp->next!=nullptr) tmp=tmp->next;
    tmp->next=new RunListElement;
    tmp->next ->data=prun;
    tmp->next ->next=nullptr;
  }
}


int RunList::size() const {
  int size=0;
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next) size++;
  return size;
}

Run* RunList::operator [] (int idx) const {
  if (idx < 0 || idx >= size()) return nullptr;
  RunListElement* tmp=head;
  while(idx!=0) {
    tmp=tmp->next;
    idx--;
  }
  return tmp->data;
}



