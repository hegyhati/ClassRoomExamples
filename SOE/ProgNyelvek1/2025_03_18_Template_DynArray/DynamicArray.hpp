#ifndef DYNAMIC_ARRAY
#define DYNAMIC_ARRAY

#include <iostream>

template <typename T>
class DynamicArray{
    T * values;
    unsigned int capacity;
    unsigned int count;

    void resize(){
        T *tmp = new T[capacity*2];
        for (unsigned int idx = 0; idx < capacity; ++idx)
            tmp[idx] = values[idx];
        delete [] values;
        values = tmp;
        capacity *= 2;
        std::cerr << "resized to " << capacity << ": "<< *this << std::endl;
    }

    void check_index(int& idx) const{
        if (idx < 0) idx += count;
        if (idx < 0 || idx >= (int) count) 
            throw OutOfBoundsException();
    }

    void shift_left(unsigned int idx){
        for (unsigned int i = idx+1; i < count; ++i)
            values[i-1] = values[i];
        --count;
    }
    
public:
    
    DynamicArray(const unsigned int capacity = 2)
        : values(new T[capacity]), capacity(capacity), count(0) {}

    DynamicArray(const DynamicArray& other)
        : values(new T[other.capacity]), capacity(other.capacity), count(other.count) {
        for (unsigned int idx = 0; idx < count; ++idx)
            values[idx] = other.values[idx];
    }

    // assignment operator!
    
    ~DynamicArray() {
        delete [] values;
        values = nullptr;
        capacity = count = 0;
    }

    T& operator[](int idx) const {
        check_index(idx);
        return values[idx];
    }

    void append(T value) {
        if (count == capacity) resize();
        values[count++] = value;
    }

    T pop(int idx = -1) {
        check_index(idx);
        T tmp = values[idx];
        shift_left(idx);
        return tmp;
    }

    unsigned int size() const { return count; }

    class OutOfBoundsException{};
};

template<typename T>
std::ostream& operator << (std::ostream& s, const DynamicArray<T>& array){
    s << "[";
    for (unsigned int idx = 0; idx < array.size(); ++idx) {
        if (idx != 0) s << ", ";
        s << array[idx];
    }
    s << "]";
    return s;
}

#endif