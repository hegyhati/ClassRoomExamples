#include <iostream>
#include <vector>
using namespace std;

struct CarState{
  double s;
  double v;
  double a;
};



CarState& getleader(CarState cars[4]){
  int max=0;
  for(int c=1;c<4;c++)
    if(cars[c].s > cars[max].s)
      max=c;
  return cars[max];
}

void leaderboard(CarState cars[4]){
  CarState bestcar=getleader(cars);
  cout<<"The leader is: Car "<< getleader(cars).name<<endl;
  for(int c=0; c<4; c++)
      cout<<"Car "<<c<<": "<< cars[c].s <<"\t";
  cout<<endl; 
}

void  carelapse(CarState& car){
  car.s+=car.v;
  car.v+=car.a;
}


void timeelapse(int& time, CarState cars[4]) {  
  time++;
  for(int c=0; c<4; c++)
    carelapse(cars[c]);
}




int main(){
  CarState cars[4] = {
      {0,0,1} ,
      {0,2,0.1} ,
      {0,-1,0.2} ,
      {6,0.5,1} };
  
  for(int t=0; t<20; timeelapse(t,cars)){
    cout<<"Time: "<<t<<"\t";
    
    leaderboard(cars);    
}

  
  return 0;

}

