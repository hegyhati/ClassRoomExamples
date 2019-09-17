#include <iostream>
#include <fstream>
using namespace std;

#include "Job.h"
#include "Schedule.h"



void printMenu(){
  cout << "Mit szeretnel?" << endl;
  cout << "  [uj] Uj rendeles felvetele" << endl;
  cout << "  [kilep] Kilepes a programbol" << endl;
}

void getNewOrder(Schedule& sch){
  
  string client;
  cout <<"Ki lusta megirni a sajat szakdogajat?"<<endl;
  cin >> client;
  int start;
  cout <<"Mikor alljunk neki?"<<endl;
  cin >> start;
  int finish;
  cout <<"Meddig dolgozzunk rajta?"<<endl;
  cin >> finish;
  Job newJob(client,start,finish);

  if(sch.feasible(newJob)) {
    cout << "Deal, megcsinaljuk." << endl;
    sch.insert(newJob);
  } else {
    cout << "Sorry bro', nem erunk ra :'(" << endl;
  }  
}


int main(){
  Schedule sch;
  sch.load("adatbazis.txt");
  string response="uj";
  while (response=="uj") {
    sch.debug();
    printMenu();
    cin >> response;
    if (response == "uj") getNewOrder(sch);
  }
  sch.save("adatbazis.txt");
  return 0;
}


