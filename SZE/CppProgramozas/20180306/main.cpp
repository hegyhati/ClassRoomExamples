#include "tester.hpp"
#include <iostream>
using namespace std;

int main(){
    Tester::setDefaultMaxD(2);
    Tester izebize(10,10);
    //Tester izebize("palya.txt")

    int dx,dy;
    
    while(!izebize.isFinished() && !izebize.isGameOver()){
        izebize.fancyPrint();
        do {
            cout<<"Lepes pleeeeeease ";
            cin>>dx;
            cin>>dy;
        } while (!izebize.move(dx,dy));        
    }
    if(izebize.isFinished()) {
        cout<<"Yepeeeeee!!!!!!!negy!!!\n";
    } else if (izebize.isGameOver()) {
        cout<<"Next time...\n";
    } else {
        cout<<"I have no idea what I'm doing\n";
    }
    return 0;
}
