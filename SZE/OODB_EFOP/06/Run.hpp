#ifndef RUN_HPP
#define RUN_HPP

#include <string>
#include <iostream>
#include "DateTime.hpp"

class Run {
  private:
    std::string name; 
    double distance;
    Time duration;   
  public:
    Run (std::string name="", double distance=0, int seconds=0);
    double getDistance() const {return distance;}
    int getDuration() const {return duration.getDuration();}
    friend std::ostream& operator << (std::ostream& s, const Run& r);
    friend std::istream& operator >> (std::istream& s, Run& r);
};



#endif
