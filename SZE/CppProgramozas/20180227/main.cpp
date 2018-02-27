#include "tester.hpp"
#include <iostream>
using namespace std;

int main(){
    Tester::setDefaultMaxD(2);
    Tester izebize(50,20);
    //Tester izebize("palya.txt")

    int dx,dy;
    
    while(!izebize.isFinished()){
        izebize.print();
        do {
            cout<<"Lepes pleeeeeease ";
            cin>>dx;
            cin>>dy;
        } while (!izebize.move(dx,dy));        
    }

    cout<<"Yay\n";
    return 0;
}
