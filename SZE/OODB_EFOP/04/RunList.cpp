#include "RunList.hpp"

#include <iostream>
using namespace std;

RunList::~RunList(){
  for(RunListElement *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head;    
  }
}

void RunList::inputRuns(){
  Run tmprun;
  do {    
    tmprun.input();
    if (tmprun.distance!=0 && tmprun.duration !=0) {
      RunListElement* tmp=new RunListElement;
      tmp->data=tmprun;
      tmp->next=head;
      head=tmp;
    }
  } while (tmprun.distance!=0 && tmprun.duration !=0);
}

void RunList::printRuns() const {
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    tmp->data.print();
  }
}

Run RunList::longestRun() const {
  Run longest={0,0};
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    if (tmp->data.distance > longest.distance) longest = tmp->data;
  }
  return longest;
}
