#include "Car.hpp"
#include <cmath>



Car::Car(double s0, double v0, double a)
  : x(s0), y(0), alpha(0), v(v0), a(a) {}
Car::Car(double x, double y, double alpha, double v0, double a)
  : x(x), y(y), alpha (alpha), v(v0), a(a) {}
  
  
void Car::elapseTime(double t) {
  x+=(v*t+a*t*t/2)*cos(alpha);
  y+=(v*t+a*t*t/2)*sin(alpha);
  v+=a*t;
}

double Car::getDist() const {
  return sqrt(x*x+y*y);      
}
