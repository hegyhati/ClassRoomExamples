#ifndef JOB_H
#define JOB_H

#include <string>
using namespace std;

class Job {
    string client;
    int start;
    int finish;
  public:
    Job();
    Job(string client, int start, int finish);
    string getClient();
    int getStart();
    int getFinish();
    bool overlaps(Job otherjob);
};

#endif
