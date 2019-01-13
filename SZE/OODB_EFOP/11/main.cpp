#include <iostream>
using namespace std;

#include "RunManager.hpp"


int main(int argc, char** argv){
  Date d;
  if (argc<2) {cout<<"Please provide a database file."<<endl;}
  else {
    // Creata manager and load data from file
    RunManager myruns(argv[1]);

    // Print data in database
    cout << "Current data in database:"<<endl;
    myruns.printAll();
  }
  return 0;
}

