#include "Car.hpp"
#include "Race.hpp"

int main(){
  Car cars[SIZE] = {
      {0,1},
      {2,0,3,2}
      };

  Race r(cars);


  
  for(; r.getLeaderDist()<10; r.elapseTime(1)){
    r.printLeaderboard();
  }
  r.printLeaderboard();
  
  return 0;

}

