#include <iostream>
using namespace std;

struct Run {
  double distance;
  double duration;
};



class RunList{
  
  private:

    struct RunListElement{
      Run data;
      RunListElement *next;
    };
  
    RunListElement* head=nullptr;
    
  public:
  
    void inputRuns(){
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

    void printRuns(){
      for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
        cout << "The run was "<<tmp->data.distance<<" km long, and it took "<<tmp->data.duration<<" seconds."<<endl;
      }
    }

    Run longestRun(){
      Run longest={0,0};
      for(RunListElement* tmp=head;tmp!=nullptr;tmp=tmp->next){
        if (tmp->data.distance > longest.distance) longest = tmp->data;
      }
      return longest;
    }

    void deleteRuns(){
      for(RunListElement *tmp; head!=nullptr; head=tmp){
        tmp=head->next;
        delete head;    
      }
    }
};



int main(){
  RunList myruns;

  // Input data
  myruns.inputRuns();

  // Output data
  myruns.printRuns();

  // Do magic
  Run longest=myruns.longestRun();
  if (longest.distance==0) cout << "You were too lazy..."<<endl;
  else cout<<"Longest run was "<<longest.distance<<" km long."<<endl;

  // Clean up the mess
  myruns.deleteRuns();

  return 0;
}

