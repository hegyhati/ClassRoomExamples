#include "Manager.hpp"
#include <iostream>

void Manager::hire(std::string employee){
  employees[employee]=Schedule();
}

std::string Manager::accept_if_suitable(const Job& newJob) {
  for(auto& employee : employees) {
    if(employee.second.suitable(newJob)) {
      employee.second.accept(newJob);
      return employee.first;
    }
  }
  return "";
}

void Manager::print() const {
  std::cout <<"Erno's Angels:"<<std::endl;
  for(auto& employee:employees){
    std::cout <<"  "<<employee.first<<std::endl;
    for(int i=0; i<employee.second.getCounter(); i++)
      std::cout << "   - Job " << i+1 << ": " << employee.second.getJob(i).getName() << " " << employee.second.getJob(i).getStartDay() << "-" << employee.second.getJob(i).getEndDay()<<std::endl;      
  }
}

