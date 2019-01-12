#include "DateTime.hpp"

std::ostream& operator << (std::ostream& s, const Date& d) {
  s << d.year << "." << d.month << "." << d.day;
  return s;
}

std::ostream& operator << (std::ostream& s, const Time& t) {
  if (t.hours() > 0) s <<" "<< t.hours() << " h";
  if (t.minutes() > 0) s <<" "<< t.minutes() << " min";
  if (t.seconds() > 0) s <<" "<< t.seconds() << " s";
  return s;
}
