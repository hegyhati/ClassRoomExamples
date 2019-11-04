#ifndef SCHEDULE_HPP
#define SCHEDULE_HPP

#include "Job.hpp"

struct Schedule{
  Job accepted[10];
  int counter;
  bool suitable(const Job& newJob) const;
  void print() const;
  void sort();
  void accept(const Job& newJob);
};


#endif
