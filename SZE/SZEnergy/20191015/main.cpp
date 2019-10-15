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

void print(Schedule person){
  for(int i=0; i<person.counter; i++)
    cout << "Job " << i+1 << ": " << person.accepted[i].name << " " << person.accepted[i].startday << "-" << person.accepted[i].startday + person.accepted[i].duration-1<<endl;
}

bool suitable(Schedule person, Job newJob){
  //TODO later
  return true;
}

void accept(Schedule& person, Job newJob){
  if (person.counter < 10 ){
    person.accepted[person.counter]=newJob;
    person.counter++;
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
    
        cerr << "RESPONSE: " << response << endl<<endl;

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

  string Name;
  cin >> Name;
  cout << Name;
  return 0;
}
