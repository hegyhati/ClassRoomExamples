#include "GPSMeasurement.hpp"


double GPSMeasurement::getY() const
{
  return y;
}

double GPSMeasurement::getX() const
{
  return x;
}

Time GPSMeasurement::getTime() const
{
  return time;
}

void GPSMeasurement::persist(std::ostream &s) const
{
  time.persist(s);
  s << " " << x << " " << y << std::endl;
}

void GPSMeasurement::loadfrom(std::istream &s)
{
  time.loadfrom(s);
  s >> x;
  s >> y;
}
