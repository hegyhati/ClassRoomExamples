#ifndef SAFE_ARRAY_HPP
#define SAFE_ARRAY_HPP

#include <list>
#include <string>
#include <sstream>



// todo: make it into a template

class SafeArray{
    int* data;
    const uint _size;
    static std::list<SafeArray*> dynamic_arrays;
  public:
    SafeArray(uint size);
    ~SafeArray();
    int& operator[](uint idx);
    uint size() const;
    
    static SafeArray* getNewSafeArray(uint size);
    static void deleteDynamicArrays();
};

struct  IndexException{
  const SafeArray* address;
  const uint index;
  std::string message() const {
    std::stringstream ss;
    ss << "Element "<<index<<" of SafeArray at address "<< address <<" can not be accessed, size of SafeArray is "<<address->size()<<".";
    return ss.str();
  }
};

#endif
