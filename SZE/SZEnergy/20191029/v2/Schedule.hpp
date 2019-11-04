#ifndef SCHEDULE_HPP
#define SCHEDULE_HPP

#include "Job.hpp"

class Schedule{
    Job accepted[10];
    int counter;
  public:
    Schedule():counter(0){}
    bool suitable(const Job& newJob) const;
    void print() const;
    void sort();
    void accept(const Job& newJob);
};


#endif
