#include <iostream>
using namespace std;

struct Run{
  double distance;
  double duration;
  Run *next;
};

void inputRuns(Run*& head){
  double dist;
  double dur;
  do {
    cin >> dist;
    cin >> dur;
    if (dist!=0 && dur !=0) {
      Run* tmp=new Run;
      tmp->distance=dist;
      tmp->duration=dur;
      tmp->next=head;
      head=tmp;
    }
  } while (dist!=0 && dur !=0);
}

void printRuns(Run*& head){
  for(Run* tmp=head;tmp!=nullptr;tmp=tmp->next){
    cout << "The run was "<<tmp->distance<<" km long, and it took "<<tmp->duration<<" seconds."<<endl;
  }
}

Run* longestRun(Run*& head){
  Run* longest=head;
  for(Run* tmp=head;tmp!=nullptr;tmp=tmp->next){
    if (tmp->distance > longest->distance) longest = tmp;
  }
  return longest;
}

void deleteRuns(Run*& head){
  for(Run *tmp; head!=nullptr; head=tmp){
    tmp=head->next;
    delete head;    
  }
}

int main(){
  Run* head=nullptr;

  // Input data
  inputRuns(head);

  // Output data
  printRuns(head);

  // Do magic
  Run* longest=longestRun(head);
  if (longest==nullptr) cout << "You were too lazy..."<<endl;
  else cout<<"Longest run was "<<longest->distance<<" km long."<<endl;

  // Clean up the mess
  deleteRuns(head);

  return 0;
}

