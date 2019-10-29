#ifndef SCHEDULE_HPP
#define SCHEDULE_HPP


#define MAXJOBCOUNT 10
#include "Job.hpp"

class Schedule{
    Job accepted[MAXJOBCOUNT];
    int counter;
  public:
    Schedule();
    bool suitable(const Job& newJob) const;
    void sort();
    void accept(const Job& newJob);
    int getCounter() const;
    Job getJob(int id) const;
    
};


#endif
