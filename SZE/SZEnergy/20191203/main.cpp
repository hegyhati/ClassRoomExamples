#include <iostream>
#include <string>
using namespace std;

#include "Job.hpp"
#include "Schedule.hpp"
#include "Manager.hpp"

int main(int argc, char** argv) {

  if (argc < 2) {
    cerr << "Please provide a database file." << endl;
    return 1;
  } 

  Manager Erno(argv[1]);

  string response;

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
