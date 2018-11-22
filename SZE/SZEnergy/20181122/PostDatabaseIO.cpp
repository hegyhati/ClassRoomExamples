#include "PostDatabase.hpp"


void PostDatabase::readFrom(istream& file){
  count=0;
  while(!file.eof()) {
    if(file >> items[count]) {
      ++count;
    } else {
      /* Handle bad input */
    }
  }
}

void PostDatabase::writeTo(ostream& s) const{
  for(int p=0; p<count; ++p) {
    s << items[p] << endl;
  }
}


