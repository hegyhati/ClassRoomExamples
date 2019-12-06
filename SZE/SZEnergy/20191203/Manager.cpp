#include "Manager.hpp"
#include <iostream>
#include <fstream>


Manager::Manager(const std::string databasefilename) {
  std::ifstream file(databasefilename);
  if(file.is_open()){
    std::string worker;
    while (!file.eof()) {
      file >> worker;
      if(!file.fail()) {
        if(hasWorker(worker)) {
          std:: cerr << "Cannot register "<<worker<<" as a worker, another worker with the same name is already registered." << std::endl;
        } else {
          hire(worker);
          std::cerr << "Register "<<worker<<" as a worker"<<std::endl;
        }
      }
    }
    file.close();
  } else {
    std::cerr << "Corrupt database file, couldn't initialize list of workers" << std::endl;
  }
}

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

bool Manager::hasWorker(const std::string workername) const {
  return (employees.count(workername) != 0);
}
