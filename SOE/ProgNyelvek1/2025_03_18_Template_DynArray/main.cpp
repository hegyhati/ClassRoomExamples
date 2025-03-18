#include "FixIntArray.hpp"
#include "DynamicIntArray.hpp"
#include "DynamicArray.hpp"
#include <iostream>

void testFixIntArray(){
    FixIntArray myArray(10);
    std::cout << myArray << std::endl;
    for (int i=0; i<myArray.size; ++i)
        myArray[i] = i*i;
    std::cout << myArray << std::endl;
}

void testDynamicIntArray() {    
    DynamicIntArray list;
    int number;
    do {
        std::cin >> number;
        list.append(number);
    } while (number != 0);
    
    std::cout << list;
    
    list.pop();
    list.pop(0);
    
    std::cout << list;
}

void testCopy(){
    DynamicIntArray myArray;
    myArray.append(2);
    myArray.append(3);
    DynamicIntArray mySecondArray = myArray;
    std::cout << myArray << mySecondArray << std::endl;
}

class Foo {
    public :
    int foo;
    int bar;
    Foo () : foo(1), bar(2) {};
};


std::ostream& operator << (std::ostream& s, const Foo& f) {
    return s << "Foo("<<f.foo<<","<<f.bar<<")";
}

int main() {
    // testFixIntArray();
    // testDynamicIntArray();
    // testCopy();

    DynamicArray<float> myFloatArray;
    myFloatArray.append(1.2);
    myFloatArray.append(4.2);
    myFloatArray.append(5.2);
    myFloatArray.append(6.2);
    std::cout << myFloatArray << std::endl;

    DynamicArray<Foo> a;
    a.append(Foo());
    a.append(Foo());
    a.append(Foo());
    a.append(Foo());
    a.append(Foo());
    std::cout << a << std::endl;


}