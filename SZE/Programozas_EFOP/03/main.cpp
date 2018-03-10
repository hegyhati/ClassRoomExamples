/*
 * Feladat:
 * Kerj be ket szamot, ird ki a nagyobbikat! 
 *
 * Peldak:
 *   3   5 -->   5
 *  -3   2 -->   2
 * -55 -36 --> -36
 *   1   1 -->   1 
 *
 */



#include<iostream>
using namespace std;

int main(){
    int a;
    int b;

    cin>>a;
    cin>>b;

    // Megoldas 1

    if (a>b) {
        cout << a << endl;
    } else {
        cout << b << endl;
    }

    // Megoldas 2
    if (a>b) cout << a << endl;
    else cout << b << endl;

    // Megoldas 3
    cout << ((a>b)?a:b) << endl; 
    
    return 0;
}

