#ifndef MANAGER_HPP
#define MANAGER_HPP

#include "Schedule.hpp"
#include "Job.hpp"
#include <string>


class Manager {
    Schedule Laci;
    Schedule Huba;
  public:
    std::string accept_if_suitable(const Job& newJob);
    void print() const;
};

#endif
