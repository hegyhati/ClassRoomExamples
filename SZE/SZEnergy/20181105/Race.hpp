#ifndef RACE_HPP
#define RACE_HPP

#include "Car.hpp"
#define SIZE 2

class Race{
    Car cars[SIZE];
  public:
    Race(Car cars[SIZE]);
    
    int getLeader() const;
    double getLeaderDist() const;
    void printLeaderboard() const;
    void elapseTime(double time=1);
};

#endif
