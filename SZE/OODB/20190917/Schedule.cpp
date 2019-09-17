#include "Schedule.h"

void Schedule::debug(){
  cerr << "\n\nOsszesen "<<count<<" megrendeles erkezett:"<<endl;
  for(int i=0; i< count; ++i)
    cerr << "\t"<<jobs[i].getClient()<<": "<<jobs[i].getStart()<<"-"<<jobs[i].getFinish()<<endl;
  cerr<<endl<<endl;
}

void Schedule::load(string databaseFileName){ 
  ifstream file(databaseFileName);
  file >> count;
  string client; int start; int finish;
  for(int j=0;j<count; j++){
    file >> client >> start >> finish;
    jobs[j] = Job(client,start,finish);
  }
}

void Schedule::save(string databaseFileName){
  ofstream file(databaseFileName);
  file << count << endl;
  for(int j=0;j<count; j++)
    file << jobs[j].getClient() << " "
         << jobs[j].getStart()  << " "
         << jobs[j].getFinish() << endl;
}

bool Schedule::feasible(Job newJob) {
  for(int j=0; j<count; ++j)
    if(newJob.overlaps(jobs[j])) return false;
  return true;
}

void Schedule::insert(Job newJob){
  jobs[count]=newJob;
  count++;
}
