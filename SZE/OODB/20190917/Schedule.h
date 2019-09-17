#ifndef SCHEDULE_H
#define SCHEDULE_H

#include <iostream>
#include <fstream>
using namespace std;

#include "Job.h"

class Schedule {
    Job jobs[100];
    int count;
  public:
    void debug();
    void load(string databaseFileName);
    void save(string databaseFileName);
    bool feasible(Job newJob);
    void insert(Job newJob);
};



#endif
