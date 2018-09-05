#include <iostream>
#include "PLItem.hpp"

int main(){
  PLItem* track=NULL;
  append(track,{1,1,0});
  append(track,{4,5,30});
  append(track,{6,5,40});
  print(track);
  std::cout<<"Length: "<<length(track)<<std::endl;
  std::cout<<"AVG Speed: "<<avgspeed(track)<<std::endl;
  reset(track);
}
