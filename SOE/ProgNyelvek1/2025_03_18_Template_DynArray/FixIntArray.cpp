#include "FixIntArray.hpp"

FixIntArray::FixIntArray(const int size) : values (new int[size]), size(size) {
    for (int idx = 0; idx < size; ++idx) 
        values[idx] = 0;
}

FixIntArray::~FixIntArray() { delete [] values; }

int& FixIntArray::operator[](int idx) const{
    if (idx >= 0 && idx < size) {
        return values[idx];
    } else {
        throw OutOfBoundsException();
    }
}

std::ostream& operator << (std::ostream& s, const FixIntArray& array){
    s << "[";
    for (int idx = 0; idx < array.size; ++idx) {
        if (idx != 0) s << ", ";
        s << array[idx];
    }
    s << "]";
    return s;
}
