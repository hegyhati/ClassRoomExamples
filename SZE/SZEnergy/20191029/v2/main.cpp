#include <iostream>
#include <string>
using namespace std;

#include "Job.hpp"
#include "Schedule.hpp"


int main() {

  string response;
  
  Schedule Erno;

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
      Job newJob(name,startday,duration);
      if(Erno.suitable(newJob)) 
        Erno.accept(newJob);
      response="";
    }
    if (ize==6) return -1;
    ize++;
  } while (response != "exit");

  return 0;
}
