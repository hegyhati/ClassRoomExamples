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
    cin >> tmprun;
    if (tmprun.getDistance()!=0 && tmprun.getDuration() !=0) {
      RunListElement* tmp=new RunListElement;
      tmp->data=tmprun;
      tmp->next=head;
      head=tmp;
    }
  } while (tmprun.getDistance()!=0 && tmprun.getDuration() !=0);
}

void RunList::printRuns() const {
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    cout<< (tmp->data) << endl;
  }
}

Run RunList::longestRun() const {
  Run longest("startingshortest",0,0);
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    if (tmp->data.getDistance()> longest.getDistance()) longest = tmp->data;
  }
  return longest;
}
