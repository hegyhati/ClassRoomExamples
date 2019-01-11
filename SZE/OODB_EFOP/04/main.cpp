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
  if (longest.distance==0) cout << "You were too lazy..."<<endl;
  else cout<<"Longest run was "<<longest.distance<<" km long."<<endl;

  return 0;
}

