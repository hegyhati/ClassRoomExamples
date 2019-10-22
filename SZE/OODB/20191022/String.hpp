#ifndef STRING_HPP
#define STRING_HPP

#include <vector>
#include <iostream>

class String{
    const int base;
    std::vector<char> text;
  public:
    String(const char*, int base=2);
    //String& operator+=(const char*);
    String& operator+=(int);
    String& operator+=(const String&);
    friend std::ostream& operator<< (std::ostream& s, const String& t);
};


#endif
