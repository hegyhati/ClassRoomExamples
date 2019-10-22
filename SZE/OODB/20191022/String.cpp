#include "String.hpp"
#include <list>


String::String(const char* ptext, int base) :base(base){
  for(const char* pt=ptext; *pt!='\0'; ++pt)
    text.push_back(*pt);
  std::cerr<<"Konstruktor"<<*this << std::endl;
}

std::ostream& operator<< (std::ostream& s, const String& t) {
  for(const auto& c: t.text)
    s << c;
  return s;
}

//String& String::operator+=(const char* ptext){
  //for(const char* pt=ptext; *pt!='\0'; ++pt)
    //text.push_back(*pt);
  //return *this;  
//}


String& String::operator+=(int number){
  if(number<0) {
    text.push_back('-');
    number*=(-1);
  }
  std::list<int> tmp;
  for(;number!=0;number/=base)
    tmp.push_front(number%base);
  for(int digit: tmp)
    text.push_back('0'+digit);
  return *this;  
}

String& String::operator+=(const String& other){
  text.insert(text.end(), other.text.begin(), other.text.end());
}
