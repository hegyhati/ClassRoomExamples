#include "Run.hpp"

Run::Run (std::string name, double distance, int seconds)
  : name(name), distance(distance), duration(seconds) {}

void Run::loadfrom(std::istream& s) {
  s>>name;
  s>>distance;
  duration.loadfrom(s);
}

void Run::persist(std::ostream& s) const {
  s << name <<"\t"<<distance<<"\t";
  duration.persist(s);
  s<<std::endl;
}

std::ostream& operator << (std::ostream& s, const Run& r) {
  s << r.name <<":\t"<<r.distance<<" km\t"<<r.duration;
  return s;
}


