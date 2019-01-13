#include "Run.hpp"

Run::Run (std::string name, double distance, int seconds)
  : name(name), distance(distance), duration(seconds) {}

void Run::loadfrom(std::istream& s) {
  date.loadfrom(s);
  s>>name;
  s>>distance;
  duration.loadfrom(s);
}

void Run::persist(std::ostream& s) const {
  date.persist(s);
  s << name <<"\t"<<distance<<"\t";
  duration.persist(s);
  s<<std::endl;
}

std::ostream& operator << (std::ostream& s, const Run& r) {
  s << r.name
    << " (" << r.date << "):\t"
    <<r.distance<<" km\t"
    <<r.duration;
  return s;
}


