#include <iostream>
#include <string>
using namespace std;

#include "Job.hpp"
#include "Schedule.hpp"


int main() {

  string response;
  
  Schedule Erno;
  Erno.counter=0;

  int ize=0;
  
  do {
    cout << endl << "Current schedule of Erno:"<<endl;
    Erno.print();
    cout << "What you gonna do?" << endl;
    cin >> response;
    if (response == "new") {
      string name;
      int startday, duration;
      cin >> name >> startday >> duration;
      Job newJob;
      newJob.setName(name);
      newJob.setStartDay(startday);
      newJob.setDuration(duration);      
      if(Erno.suitable(newJob)) 
        Erno.accept(newJob);
      response="";
    }
    if (ize==6) return -1;
    ize++;
  } while (response != "exit");

  return 0;
}
