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
  
    void inputRuns();
    void printRuns();
    Run longestRun();
    void deleteRuns();
};

#endif
