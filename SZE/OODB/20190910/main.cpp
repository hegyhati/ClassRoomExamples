#include <iostream>
#include <fstream>
using namespace std;

struct Job {
  string client;
  int start;
  int finish;
};

struct Schedule {
  Job jobs[100];
  int count;
};

void debug(Schedule sch){
  cerr << "\n\nOsszesen "<<sch.count<<" megrendeles erkezett:"<<endl;
  for(int i=0; i< sch.count; ++i)
    cerr << "\t"<<sch.jobs[i].client<<": "<<sch.jobs[i].start<<"-"<<sch.jobs[i].finish<<endl;
  cerr<<endl<<endl;
}

Schedule load(string databaseFileName){
  Schedule toReturn;
  ifstream file(databaseFileName);
  file >> toReturn.count;
  for(int j=0;j<toReturn.count; j++)
    file >> toReturn.jobs[j].client
         >> toReturn.jobs[j].start
         >> toReturn.jobs[j].finish;
  return toReturn;
}

void save(Schedule sch, string databaseFileName){
  ofstream file(databaseFileName);
  file << sch.count << endl;
  for(int j=0;j<sch.count; j++)
    file << sch.jobs[j].client << " "
         << sch.jobs[j].start  << " "
         << sch.jobs[j].finish << endl;
}

void printMenu(){
  cout << "Mit szeretnel?" << endl;
  cout << "  [uj] Uj rendeles felvetele" << endl;
  cout << "  [kilep] Kilepes a programbol" << endl;
}

bool overlaps(Job j1, Job j2) {
  return j2.start <= j1.finish && j2.finish>=j1.start;
}

bool feasible(Schedule sch, Job newJob) {
  for(int j=0; j<sch.count; ++j)
    if(overlaps(sch.jobs[j],newJob)) return false;
  return true;
}

void insert(Schedule& sch, Job newJob){
  sch.jobs[sch.count]=newJob;
  sch.count++;
}


void getNewOrder(Schedule& sch){
  Job newJob;
  cout <<"Ki lusta megirni a sajat szakdogajat?"<<endl;
  cin >>  newJob.client;
  cout <<"Mikor alljunk neki?"<<endl;
  cin >>  newJob.start;
  cout <<"Meddig dolgozzunk rajta?"<<endl;
  cin >>  newJob.finish;

  if(feasible(sch,newJob)) {
    cout << "Deal, megcsinaljuk." << endl;
    insert(sch,newJob);
  } else {
    cout << "Sorry bro', nem erunk ra :'(" << endl;
  }  
}


int main(){
  Schedule sch=load("adatbazis.txt");
  string response="uj";
  while (response=="uj") {
    debug(sch);
    printMenu();
    cin >> response;
    if (response == "uj") getNewOrder(sch);
  }
  save(sch,"adatbazis.txt");
  return 0;
}


