#ifndef SCHEDULE_HPP
#define SCHEDULE_HPP


#include <vector>
#include "Job.hpp"

class Schedule{
    std::vector<Job> accepted;
  public:
    Schedule();
    bool suitable(const Job& newJob) const;
    void sort();
    void accept(const Job& newJob);
    int getCounter() const;
    Job getJob(uint indx) const;
    
};


#endif
