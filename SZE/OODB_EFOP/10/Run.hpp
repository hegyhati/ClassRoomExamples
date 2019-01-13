#ifndef RUN_HPP
#define RUN_HPP

#include <string>
#include <iostream>
#include "DateTime.hpp"
#include "Persistable.hpp"

class Run : public Persistable {

  private:
    Date date;
    std::string name; 
    double distance;
    Time duration;   

  public:

    Run (std::string name="", double distance=0, int seconds=0);

    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;

    double getDistance() const {return distance;}
    int getDuration() const {return duration.getDuration();}

    friend std::ostream& operator << (std::ostream& s, const Run& r);
};



#endif
