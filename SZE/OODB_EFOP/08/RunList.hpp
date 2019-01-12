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
    void persist(std::string filename) const;
    void loadfrom(std::string filename);

    friend std::istream& operator >> (std::istream&  s, RunList& rl);
    friend std::ostream& operator << (std::ostream&  s, const RunList& rl);

    int size() const;
    Run operator [] (int idx) const ;
};

#endif
