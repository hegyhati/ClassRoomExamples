#include <iostream>
#include <string>
using namespace std;


struct Job{
  string name;
  int startday;
  int duration;
};


struct Schedule{
  Job accepted[10];
  int counter;
};

void print(const Schedule& person){
  for(int i=0; i<person.counter; i++)
    cout << "Job " << i+1 << ": " << person.accepted[i].name << " " << person.accepted[i].startday << "-" << person.accepted[i].startday + person.accepted[i].duration-1<<endl;
}

bool overlap(const Job& j1,const Job& j2){
  return (j1.startday+j1.duration-1>=j2.startday) && (j2.startday+j2.duration-1>=j1.startday);
}

bool suitable(const Schedule& person,const Job& newJob){
  for(int i=0;i<person.counter;i++)
    if(overlap(person.accepted[i],newJob)) return false;
  return true;
}

void sort(Schedule& person) {
  for(int i=0; i<person.counter; ++i) {
    for (int j=0; j<person.counter-1-i; ++j){
      if(person.accepted[j+1].startday < person.accepted[j].startday){
        Job tmp = person.accepted[j];
        person.accepted[j]=person.accepted[j+1];
        person.accepted[j+1]=tmp;
      }
    }      
  }  
}

void accept(Schedule& person, const Job& newJob){
  if (person.counter < 10 ){
    person.accepted[person.counter]=newJob;
    person.counter++;
    sort(person);
  } else {
    cout << " Person is overloaded (or lazy) " << endl;
  }
}





int main() {

  string response;
  
  Schedule Erno;
  Erno.counter=0;

  int ize=0;
  
  do {
    cout << endl << "Current schedule of Erno:"<<endl;
    print(Erno);
    cout << "What you gonna do?" << endl;
    cin >> response;
    if (response == "new") {
      Job newJob;
      cin >> newJob.name >> newJob.startday >> newJob.duration;
      if(suitable(Erno,newJob)) 
        accept(Erno,newJob);
      response="";
    }
    if (ize==6) return -1;
    ize++;
  } while (response != "exit");

  return 0;
}
