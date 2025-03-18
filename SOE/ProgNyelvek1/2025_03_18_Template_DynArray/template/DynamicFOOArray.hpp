#ifndef DYNAMIC_FOO_ARRAY
#define DYNAMIC_FOO_ARRAY

#include <iostream>

class DynamicFooArray{
        Foo * values;
        int capacity;
        int count;

        void resize();
        void check_index(int& idx) const;
        void shift_left(int idx);
        
    public:
        
        DynamicFooArray(const int capacity = 2);
        DynamicFooArray(const DynamicFooArray& other);
        // assignment operator!
        ~DynamicFooArray();
        Foo& operator[](int idx) const;
        void append(Foo value);
        Foo pop(int idx = -1);
        int size() const;

        class OutOfBoundsException{};
    };
    
std::ostream& operator << (std::ostream& s, const DynamicFooArray& array);
    
#endif