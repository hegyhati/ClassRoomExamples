#include "Schedule.hpp"
#include <iostream>

void print(const Schedule& person){
  for(int i=0; i<person.counter; i++)
    std::cout << "Job " << i+1 << ": " << person.accepted[i].name << " " << person.accepted[i].startday << "-" << person.accepted[i].startday + person.accepted[i].duration-1<<std::endl;
}

bool suitable(const Schedule& person,const Job& newJob){
  for(int i=0;i<person.counter;i++)
    if(person.accepted[i].overlaps(newJob)) return false;
  return true;
}



void sort(Schedule& person) {
  for(int i=0; i<person.counter; ++i) {
    for (int j=0; j<person.counter-1-i; ++j){
      if(person.accepted[j+1].startday < person.accepted[j].startday){
        Job tmp = person.accepted[j];
        person.accepted[j]=person.accepted[j+1];
        person.accepted[j+1]=tmp;
      }
    }      
  }  
}

void accept(Schedule& person, const Job& newJob){
  if (person.counter < 10 ){
    person.accepted[person.counter]=newJob;
    person.counter++;
    sort(person);
  } else {
    std::cout << " Person is overloaded (or lazy) " << std::endl;
  }
}
