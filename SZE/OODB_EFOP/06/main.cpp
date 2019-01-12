#include <iostream>
using namespace std;

#include "Run.hpp"
#include "RunList.hpp"

int main(){
  RunList myruns;

  // Input data
  myruns.inputRuns();

  // Output data
  myruns.printRuns();

  // Do magic
  Run longest=myruns.longestRun();
  if (longest.getDistance()==0) cout << "You were too lazy..."<<endl;
  else cout<<"Longest run was "<<longest.getDistance()<<" km long."<<endl;

  return 0;
}

