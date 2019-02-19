#include "zigzag.h"
#include <iostream>
using std::cout;
using std::endl;

int zigzag::getNumber() const { return number; }

double zigzag::length() const {
  double length = 0;
  for (int i = 1; i < next; i++)
    length += points[i] - points[i - 1];
  return length;
}

zigzag::zigzag(int number)
    : number(number), points(new Point[number]), next(0) {}

zigzag::~zigzag() { delete[] points; }

void zigzag::addPoint(double x, double y) {
  if (next < number) {
    points[next] = Point(x, y);
    ++next;
  }
}

std::ostream &operator<<(std::ostream &s, const zigzag &z) {
  for (int i = 0; i < z.next; ++i) {
    if (i)
      s << " -- ";
    s << z.points[i];
  }
  for (int i = z.next; i < z.number; ++i) {
    if (i)
      s << " -- ";
    s << "(?,?)";
  }
  return s;
}
