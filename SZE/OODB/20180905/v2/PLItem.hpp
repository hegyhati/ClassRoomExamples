#ifndef PLITEM_HPP
#define PLITEM_HPP

#include "Point.hpp"

struct PLItem {
  Point p;
  PLItem* next;
};

void append(PLItem*& track, Point p);

void print(PLItem* track);

void reset(PLItem*& track);

double length(PLItem* track);

double avgspeed(PLItem* track);

#endif
