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

    void persist(std::ostream& s) const;
    void loadfrom(std::istream& s);

    double getDistance() const {return distance;}
    int getDuration() const {return duration.getDuration();}

    friend std::ostream& operator << (std::ostream& s, const Run& r);
};



#endif
