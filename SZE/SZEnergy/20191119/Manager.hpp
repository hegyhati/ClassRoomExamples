#ifndef MANAGER_HPP
#define MANAGER_HPP

#include "Schedule.hpp"
#include "Job.hpp"
#include <string>
#include <map>

class Manager {
    std::map< std::string, Schedule > employees;
  public:
    void hire(std::string name);
    std::string accept_if_suitable(const Job& newJob);
    void print() const;
};

#endif
