#include "ManualRun.hpp"


void ManualRun::loadfrom(std::istream& s) {
  date.loadfrom(s);
  s>>name;
  s>>distance;
  duration.loadfrom(s);
}

ManualRun::ManualRun() : Run("m")
{

}

void ManualRun::persist(std::ostream& s) const {
  date.persist(s);
  s << name <<"\t"<<distance<<"\t";
  duration.persist(s);
  s<<std::endl;
}

std::ostream& operator << (std::ostream& s, const ManualRun& r) {
  s << r.name
    << " (" << r.date << "):\t"
    <<r.distance<<" km\t"
    <<r.duration;
  return s;
}


