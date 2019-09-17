#include "Job.h"

Job::Job() {
  this->client = "";
  this->start = 0;
  this->finish = 0;
}

Job::Job(string client, int start, int finish) {
  this->client = client;
  this->start = start;
  this->finish = finish;
}

bool Job::overlaps(Job otherjob) {
  return otherjob.start <= finish && otherjob.finish>=start;
}

string Job::getClient(){ return client; }
int Job::getStart(){ return start; }
int Job::getFinish(){ return finish; }
