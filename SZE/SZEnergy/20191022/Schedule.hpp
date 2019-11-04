#ifndef SCHEDULE_HPP
#define SCHEDULE_HPP

#include "Job.hpp"

struct Schedule{
  Job accepted[10];
  int counter;
};

void print(const Schedule& person);
bool suitable(const Schedule& person,const Job& newJob);
void sort(Schedule& person);
void accept(Schedule& person, const Job& newJob);


#endif
