#include "Schedule.hpp"
#include <iostream>

void Schedule::print() const{
  for(int i=0; i<counter; i++)
    std::cout << "Job " << i+1 << ": " << accepted[i].getName() << " " << accepted[i].getStartDay() << "-" << accepted[i].getStartDay() + accepted[i].getDuration()-1<<std::endl;
}

bool Schedule::suitable(const Job& newJob) const{
  for(int i=0;i<counter;i++)
    if(accepted[i].overlaps(newJob)) return false;
  return true;
}
void Schedule::sort() {
  for(int i=0; i<counter; ++i) {
    for (int j=0; j<counter-1-i; ++j){
      if(accepted[j+1].getStartDay() < accepted[j].getStartDay()){
        Job tmp = accepted[j];
        accepted[j]=accepted[j+1];
        accepted[j+1]=tmp;
      }
    }      
  }  
}

void Schedule::accept( const Job& newJob){
  if (counter < 10 ){
    accepted[counter]=newJob;
    counter++;
    sort();
  } else {
    std::cout << " Person is overloaded (or lazy) " << std::endl;
  }
}

