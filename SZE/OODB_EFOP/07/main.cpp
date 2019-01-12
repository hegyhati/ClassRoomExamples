#include <iostream>
using namespace std;

#include "Run.hpp"
#include "RunList.hpp"


int main(){
  RunList myruns;

  // Input data from database
  myruns.loadfrom("Data.txt");


  // Print data in database
  cout << "Current data in database:"<<endl;
  cout << myruns;

  // Do magic
  {
    Run longest=myruns.longestRun();
    if (longest.getDistance()==0) cout << "You were too lazy..."<<endl;
    else cout<<"Longest run was "<<longest.getDistance()<<" km long."<<endl;
  }

  // Input addtional runs from terminal
  cout << "Please add additional runs in the format of NAME DISTANCE DURATION"<<endl;
  cin >> myruns;

  // Print data in memory
  cout << "Current data in memory:"<<endl;
  cout << myruns;

  // Do magic
  {
    Run longest=myruns.longestRun();
    if (longest.getDistance()==0) cout << "You were too lazy..."<<endl;
    else cout<<"Longest run was "<<longest.getDistance()<<" km long."<<endl;
  }

  // Persist data to database
  myruns.persist("Data.txt");
  

  return 0;
}

