#include "Schedule.hpp"

Schedule::Schedule():counter(0){}

bool Schedule::suitable(const Job& newJob) const{
  if (counter==MAXJOBCOUNT) return false;
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
  if ( suitable(newJob) ){
    accepted[counter]=newJob;
    counter++;
    sort();
  } 
}

int Schedule::getCounter() const {return counter;}

Job Schedule::getJob(int id) const {
  if (id >= 0 && id < counter) return accepted[id];
  else return Job("error");
}
