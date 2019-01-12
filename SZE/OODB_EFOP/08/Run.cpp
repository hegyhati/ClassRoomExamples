#include "Run.hpp"

Run::Run (std::string name, double distance, int seconds)
  : name(name), distance(distance), duration(seconds) {}

std::istream& operator >> (std::istream& s, Run& r){
  int dur;
  s>>r.name;
  s>>r.distance;
  s>>dur;
  r.duration.setDuration(dur);
  return s;
}

void Run::loadfrom(std::istream& s) {
  s >> *this;
}

std::ostream& operator << (std::ostream& s, const Run& r) {
  s << r.name <<":\t"<<r.distance<<" km\t"<<r.duration;
  return s;
}

void Run::persist(std::ostream& s) const {
  s << name <<"\t"<<distance<<"\t"<<duration.getDuration()<<std::endl;
}
