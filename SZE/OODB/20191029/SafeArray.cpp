#include "SafeArray.hpp"

#include <iostream>
#include <algorithm>

SafeArray::SafeArray(uint size):data(new int[size]),_size(size){}
SafeArray::~SafeArray(){
  delete [] data;
  auto it=std::find(dynamic_arrays.begin(), dynamic_arrays.end(), this);
  if(it != dynamic_arrays.end()) {
    std::cerr<<"Delete called for:"<<this<<std::endl;
    dynamic_arrays.erase(it);
  }
}

std::list<SafeArray*> SafeArray::dynamic_arrays;

int& SafeArray::operator[](uint idx){
  if(idx<_size) return data[idx];
  else throw IndexException{this,idx};
}

uint SafeArray::size() const {return _size;}

SafeArray* SafeArray::getNewSafeArray(uint size){
  SafeArray* toReturn = new SafeArray(size);
  dynamic_arrays.push_back(toReturn);
  return toReturn;
}

void SafeArray::deleteDynamicArrays() {
  std::cerr<<"Deleting dynamically allocated safe arrays..."<<std::endl;
  while(!dynamic_arrays.empty()){
    std::cerr<<" - at "<<dynamic_arrays.front()<<"... ";
    delete dynamic_arrays.front();
  }
  dynamic_arrays.clear();
}
 
