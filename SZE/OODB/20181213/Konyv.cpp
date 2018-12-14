#include "Konyv.h"

#ifdef _MSC_VER
#include <ciso646>
#endif

std::ostream& operator << (std::ostream& s, const Konyv& k){
  s<<k.toString();
  return s;
}


bool Konyv::operator<(const Konyv& other) const{
  return (szerzo<other.szerzo or (szerzo==other.szerzo and cim<other.cim));
}
