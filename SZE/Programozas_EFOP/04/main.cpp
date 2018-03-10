/*
 * Feladat:
 * Kerj be ket szamot, ird ki a hanyadosukat!
 *
 * Pelda:
 *  8   2   --> 4
 *  6   -3  --> -2
 *  9   5   --> 1.8
 *  3   0   --> Vilagvege
 *  3.2 2   --> 1.6 
 *
 */



#include<iostream>
using namespace std;

int main(){
    double a;
    double b;

    cin>>a;
    cin>>b;

    if (b==0) cout <<"Vilagvege\n";
    else cout << a/b << endl;
    
    return 0;
}

