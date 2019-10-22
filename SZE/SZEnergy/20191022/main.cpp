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
