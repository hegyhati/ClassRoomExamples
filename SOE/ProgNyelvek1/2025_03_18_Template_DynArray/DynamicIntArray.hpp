#ifndef DYNAMIC_INT_ARRAY
#define DYNAMIC_INT_ARRAY

#include <iostream>

class DynamicIntArray{
        int * values;
        int capacity;
        int count;

        void resize();
        void check_index(int& idx) const;
        void shift_left(int idx);
        
    public:
        
        DynamicIntArray(const int capacity = 2);
        DynamicIntArray(const DynamicIntArray& other);
        // assignment operator!
        ~DynamicIntArray();
        int& operator[](int idx) const;
        void append(int value);
        int pop(int idx = -1);
        int size() const;

        class OutOfBoundsException{};
    };
    
std::ostream& operator << (std::ostream& s, const DynamicIntArray& array);
    
#endif