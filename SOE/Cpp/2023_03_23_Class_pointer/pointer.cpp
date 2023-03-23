#include <iostream>
using std::cout;
using std::endl;


void python(){
    /*
    a = 3
    b = a
    a = 4
    */

    // a = 3
    int* a = new int;
    *a = 3;

    // b = a
    int* b = a;

    // a = 4
    a = new int;
    *a = 4;

    
}


int main(){
    int a = 3;
    cout << &a << endl;

    int t[3];
    cout << t << endl;
    cout << &t[0] << " " << &t[1] << " " << &t[2] << endl;

    cout << t + 2 << endl;

    // t[2]  cime t + 2

    int *pa;
    pa = &a;
    a = 4;
    *(pa+4) = 6;

    cout << "&pa "<< &pa << endl;
    cout << "pa  "<< pa << endl;
    cout << "*pa "<< *pa << endl;

    python();

}