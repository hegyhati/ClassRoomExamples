#include <iostream>
#include <string>
using namespace std;

#include "Job.hpp"
#include "Schedule.hpp"
#include "Manager.hpp"

int main() {

  string response;
  
  Manager Erno;

  Erno.hire("Jancsi");
  Erno.hire("Huba");
  Erno.hire("Joco");


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
      string assigned = Erno.accept_if_suitable(newJob);
      if ( assigned == "" )
        cout << "Sorry bro' noone can do it" << endl;
      else
        cout << "Okee dokeey, "<<assigned<<" will do it"<<endl;
    }
  } while (response != "exit");

  return 0;
}
