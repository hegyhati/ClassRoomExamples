#include <iostream>
#include <string>
using namespace std;

#include "Job.hpp"

#include "LL_template.hpp"

int main(){
  LL_Job list; 
  int s; int d; string name;
  do{
    cin >> name >> s >> d;
    if(name!="exit") list.push_back(Job(name,s,d));
  } while (name!="exit");


  while(!list.empty()) {
    cout << list.front()->getName() << ": " << list.front()->getStartDay() << "-" << list.front()->getEndDay()<<endl;
    list.pop_front();
  }
  
  cout << endl;

  return 0;
}
