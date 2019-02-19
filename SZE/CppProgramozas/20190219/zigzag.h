#ifndef ZIGZAG_H
#define ZIGZAG_H

#include "point.h"

class zigzag {
  const int number;
  Point *const points;
  int next;

public:
  zigzag(int number = 1);
  ~zigzag();
  void addPoint(double x, double y);
  int getNumber() const;
  double length() const;

  friend std::ostream &operator<<(std::ostream &s, const zigzag &z);
};

#endif // ZIGZAG_H
