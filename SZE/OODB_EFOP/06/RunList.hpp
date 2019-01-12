#ifndef RUNLIST_HPP
#define RUNLIST_HPP

#include "Run.hpp"

class RunList{
  
  private:

    struct RunListElement{
      Run data;
      RunListElement *next;
    };
  
    RunListElement* head=nullptr;
    
  public:
    ~RunList();
    void inputRuns();
    void printRuns() const;
    Run longestRun() const;
};

#endif
