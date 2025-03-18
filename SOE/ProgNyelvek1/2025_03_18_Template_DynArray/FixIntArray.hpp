#ifndef FIX_INT_ARRAY
#define FIX_INT_ARRAY

#include <iostream>

class FixIntArray{
        int * const values;
        
    public:
        const int size;
        
        FixIntArray(const int size);
        ~FixIntArray();
        int& operator[](int pos) const;

        class OutOfBoundsException{};
    };
    
std::ostream& operator << (std::ostream& s, const FixIntArray& array);
    
#endif