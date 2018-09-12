#ifndef TRACK_HPP
#define TRACK_HPP

#include "Point.hpp"

struct PLItem {
  Point point;
  PLItem* next;
};

class Track {
    PLItem* track;
  public:
    Track();
    ~Track();
    void append(double x, double y, double t);
    void print() const;
    double length() const;
};


#endif
