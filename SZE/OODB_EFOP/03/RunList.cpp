#include "RunList.hpp"

#include <iostream>
using namespace std;


void RunList::inputRuns(){
  double dist;
  double dur;
  do {
    cin >> dist;
    cin >> dur;
    if (dist!=0 && dur !=0) {
      RunListElement* tmp=new RunListElement;
      tmp->data.distance=dist;
      tmp->data.duration=dur;
      tmp->next=head;
      head=tmp;
    }
  } while (dist!=0 && dur !=0);
}

void RunList::printRuns(){
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    cout << "The run was "<<tmp->data.distance<<" km long, and it took "<<tmp->data.duration<<" seconds."<<endl;
  }
}

Run RunList::longestRun(){
  Run longest={0,0};
  for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
    if (tmp->data.distance > longest.distance) longest = tmp->data;
  }
  return longest;
}

void RunList::deleteRuns(){
  for(RunListElement *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head;    
  }
}
