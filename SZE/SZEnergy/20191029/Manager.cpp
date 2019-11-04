#include "Manager.hpp"
#include <iostream>

std::string Manager::accept_if_suitable(const Job& newJob) {
  if(Laci.suitable(newJob)) {Laci.accept(newJob);return "Laci";}
  else if(Huba.suitable(newJob)) {Huba.accept(newJob);return "Huba";}
  else return "";
}

void Manager::print() const {
  std::cout <<"Erno's Angels:"<<std::endl;
  std::cout <<"  Laci"<<std::endl;
  for(int i=0; i<Laci.getCounter(); i++)
    std::cout << "   - Job " << i+1 << ": " << Laci.getJob(i).getName() << " " << Laci.getJob(i).getStartDay() << "-" << Laci.getJob(i).getEndDay()<<std::endl;    
  std::cout <<"  Huba"<<std::endl; 
  for(int i=0; i<Huba.getCounter(); i++)
    std::cout << "   - Job " << i+1 << ": " << Huba.getJob(i).getName() << " " << Huba.getJob(i).getStartDay() << "-" << Huba.getJob(i).getEndDay()<<std::endl;  
}

