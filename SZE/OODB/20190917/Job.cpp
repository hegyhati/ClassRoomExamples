#include "Job.h"


Job::Job(string client, int start, int finish)
  : client(client), start(start), finish(finish){
  if(finish<start) this->finish=start;
}

bool Job::overlaps(const Job& otherjob) {
  return otherjob.start <= finish && otherjob.finish>=start;
}

string Job::getClient() const { return client; }
int Job::getStart() const { return start; }
int Job::getFinish() const { return finish; }
