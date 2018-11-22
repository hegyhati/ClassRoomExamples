#include "PostDatabase.hpp"


void PostDatabase::readFrom(istream& file){
  count=0;
  while(!file.eof()) {
    if(items[count].readFrom(file)) {
      ++count;
    } else {
      /* Handle bad input */
    }
  }
}

void PostDatabase::writeTo(ostream& s) const{
  for(int p=0; p<count; ++p) {
    items[p].writeTo(s);
  }
}


