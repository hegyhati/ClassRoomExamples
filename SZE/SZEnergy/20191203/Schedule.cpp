#include "Schedule.hpp"
#include <algorithm>

Schedule::Schedule(){}

bool Schedule::suitable(const Job& newJob) const {
  //for(std::vector<Job>::const_iterator  it=accepted.cbegin();it!=accepted.cend();++it)
  //for(auto  it=accepted.cbegin();it!=accepted.cend();++it)
    //if((*it).overlaps(newJob)) return false;
  // for(const Job& job: accepted)
  for(auto job: accepted)
    if(job.overlaps(newJob)) return false;
  return true;
}

void Schedule::sort() {
  std::sort(accepted.begin(),accepted.end(),Job::earlier);
  std::sort(accepted.begin(),accepted.end(),
    [](const Job& first, const Job& second){
      return first.getStartDay()<second.getStartDay();
    });
}

void Schedule::accept( const Job& newJob){
  if ( suitable(newJob) ){
    accepted.push_back(newJob);
    sort();
  } 
}

int Schedule::getCounter() const {return accepted.size();}

Job Schedule::getJob(uint id) const {
  if (id < accepted.size()) return accepted[id];
  else return Job("error");
}
