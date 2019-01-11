#include "Run.hpp"

#include <iostream>

void Run::input(){
  do {
    std::cin>>distance;
    std::cin>>duration;
    std::cin>>name;
  } while (duration<0 || distance<0);
}

void Run::print() const {
  std::cout << name <<":"<<distance<<" km\t"<<duration<<" s"<<std::endl;
}
