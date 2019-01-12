#include <iostream>
using namespace std;

#include "Run.hpp"
#include "RunList.hpp"


int main(int argc, char** argv){
  if (argc<2) {cout<<"Please provide a database file."<<endl;}
  else {
    RunList myruns;

    // Input data from database
    myruns.loadfrom(argv[1]);


    // Print data in database
    cout << "Current data in database:"<<endl;
    cout << myruns;

    // Input addtional runs from terminal
    cout << "Please add additional runs in the format of NAME DISTANCE DURATION"<<endl;
    cin >> myruns;

    // Print data in memory
    cout << "Current data in memory:"<<endl;
    cout << myruns;

    // Do magic
    {
      int longestid=0;
      for(int i=1;i<myruns.size();i++) {
        if (myruns[i].getDistance() > myruns[longestid].getDistance())
          longestid=i;
      }
      cout << endl << "The longest run:" << myruns[longestid] << endl;
    }

    // Persist data to database
    myruns.persist(argv[1]);
  }

  return 0;
}

