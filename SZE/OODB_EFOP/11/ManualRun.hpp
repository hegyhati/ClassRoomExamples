#ifndef MANUALRUN_HPP
#define MANUALRUN_HPP

#include <string>
#include <iostream>
#include "DateTime.hpp"
#include "Run.hpp"

class ManualRun : public Run {

  private:
    double distance;
    Time duration;   

  public:
    ManualRun();
    virtual void persist(std::ostream& s) const override;
    virtual void loadfrom(std::istream& s) override;

    virtual double getDistance() const override {return distance;}
    virtual Time getDuration() const override {return duration;}

    friend std::ostream& operator << (std::ostream& s, const ManualRun& r);
};



#endif
