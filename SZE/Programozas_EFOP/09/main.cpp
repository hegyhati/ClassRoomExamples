/*
 * Feladat: Kerj be egy karaktert, es ket szamot: a, b.
 * a-rol es b-rol feltetelezhetjuk, hogy pozitiv egeszek.
 * Rajzolj ki egy a x b meretu teglalapot a bekert karakterbol.
 *
 * Pelda:
 * 
 * X 5 3
 *
 * XXXXX
 * XXXXX
 * XXXXX
 *
 */



#include<iostream>
using namespace std;

int main(){
    char c;
    int height, width;
    cin >>c>>width>>height;

    for(int h=0;h<height;h++) {
        for(int w=0;w<width;w++)
            cout<<c;
        cout << "\n";
    }

    return 0;
}

