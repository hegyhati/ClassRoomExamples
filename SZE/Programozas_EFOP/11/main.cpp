/*
 * Kerj be egy szamot.
 * Rajzolj ki egy ekkora meretu haromszoget az alabbi peldanak megfeleloen.
 *
 * Pelda:
 * 
 * 5
 *
 * XXXXX
 * XXXX
 * XXX
 * XX
 * X
 *
 */


#include<iostream>
using namespace std;

int main(){
    int size;    

    do {
        cin >> size;
    } while (size<1);

    for(int row=0;row<size;row++) {
        for(int x=0; x<size-row; x++)
            cout << "X";
        cout << endl;
    }

    return 0;
}

