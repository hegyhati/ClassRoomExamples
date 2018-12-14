#include "Konyv.h"

std::ostream& operator << (std::ostream& s, const Konyv& k){
  s<<k.toString();
  return s;
}


bool Konyv::operator<(const Konyv& other) const{
  return (szerzo<other.szerzo or  (szerzo==other.szerzo and cim<other.cim));
}
