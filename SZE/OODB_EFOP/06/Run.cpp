#include "Run.hpp"

Run::Run (std::string name, double distance, int seconds)
  : name(name), distance(distance), duration(seconds) {}

std::istream& operator >> (std::istream& s, Run& r){
  int dur;
  do {
    s>>r.name;
    s>>r.distance;
    s>>dur;
  } while (dur<0 || r.distance<0);
  r.duration.setDuration(dur);
  return s;
}

std::ostream& operator << (std::ostream& s, const Run& r) {
  s << r.name <<":\t"<<r.distance<<" km\t"<<r.duration;
  return s;
}
