#ifndef RUNLIST_HPP
#define RUNLIST_HPP

#include "Run.hpp"
#include <iostream>
#include <string>

class RunList{
  
  private:

    struct RunListElement{
      Run data;
      RunListElement *next;
    };
  
    RunListElement* head=nullptr;
    
  public:
    ~RunList();

    void add(Run run);
    int size() const;
    Run operator [] (int idx) const ;
};

#endif
