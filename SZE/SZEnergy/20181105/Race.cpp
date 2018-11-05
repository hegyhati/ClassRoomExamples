#include "Race.hpp"
#include <iostream>
using namespace std;

Race::Race(Car cars[SIZE]) {    
  for(int c=0;c<SIZE;c++)
    this->cars[c]=cars[c];
}

int Race::getLeader() const {
  int max=0;
  for(int c=1;c<SIZE;c++)
    if(cars[c].getDist() > cars[max].getDist())
      max=c;
  return max;
}

double Race::getLeaderDist() const {
  return cars[getLeader()].getDist();
}

void Race::printLeaderboard() const {
  //cout<<"The leader is: Car "<< getleader(cars)<<endl;
  for(int c=0; c<SIZE; c++)
      cout<<"Car "<<c<<": "<< cars[c].getDist() <<"\t";
  cout<<endl; 
}

void Race::elapseTime(double time) {  
  for(int c=0; c<SIZE; c++)
    cars[c].elapseTime(time);
} 
