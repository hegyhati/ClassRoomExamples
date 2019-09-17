#ifndef JOB_H
#define JOB_H

#include <string>
using namespace std;

class Job {
    string client;
    int start;
    int finish;
  public:
    Job(string client="", int start=0, int finish=0);
    string getClient() const;
    int getStart() const;
    int getFinish() const;
    bool overlaps(const Job& otherjob);
};

#endif
