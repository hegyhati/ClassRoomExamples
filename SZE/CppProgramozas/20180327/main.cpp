#include <iostream>
using namespace std;

#include "tower.hpp"

int main(){
    Tower t1(3,4,1.4,2.3);
    Tower t2(t1);    
    cout<<"t1: "; t1.testPrint();
    cout<<"t2: "; t2.testPrint();

    cout<<"t2.setMeh(4)\n";
    t2.setMeh(4);
    cout<<"t1: "; t1.testPrint();
    cout<<"t2: "; t2.testPrint();
    
    return 0;
}
