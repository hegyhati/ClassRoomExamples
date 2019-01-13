#ifndef RUNMANAGER_HPP
#define RUNMANAGER_HPP

#include <string>
#include "RunList.hpp"
#include "GPSRun.hpp"

class RunManager
{
  private:
    std::string filename;
    RunList data;
  public:
    RunManager(std::string databasefilename);
    ~RunManager();

    void persist() const;

    void printAll(std::ostream &s=std::cout) const;
};

#endif // RUNMANAGER_HPP
