#include "itoa.hpp"

std::string toString(int x){
    std::string toReturn="";
    while(x>0) {
        toReturn.insert(toReturn.begin(),(char) ('0'+x%10));
        x/=10;
    }
    return toReturn;
}
