#include <iostream>
#include <string>
using namespace std;

#include "SafeArray.hpp"

void debugArray(SafeArray& array) {
  for(uint i=0; i<array.size(); ++i)
    cout << &array << " ["<<i<<"]="<<array[i]<<endl;
}


int main(){
  SafeArray a1(12);  
  SafeArray* pa1= SafeArray::getNewSafeArray(15);
  SafeArray* pa2= SafeArray::getNewSafeArray(30);
  try {
    a1[3]=4;
    debugArray(a1);
    a1[23]=4;
    debugArray(a1);
  } catch (IndexException e) {
    cerr <<"Index exception caught:" << endl
         <<"-----------------------" << endl
         <<"  "<< e.message() << endl;
  }

  delete pa1;  
  SafeArray::deleteDynamicArrays();
  return 0;
}
