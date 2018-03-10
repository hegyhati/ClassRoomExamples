/*
 * Feladat: Kerj be harom szamot: a,b.
 * Ird ki a Fibonacci szamokat az [a,b] intervallumban
 * 
 *
 * Pelda:
 * 10 100 --> 13 21 34 55 89
 *
 */


#include<iostream>
using namespace std;

int main(){
    int min, max;
    cin >> min >> max;

    int f1, f2, f3;
    f1=0;
    f2=1;
    f3=f2+f1;
    while (f3 <= max) {
        if (min<=f3) cout << f3 << " ";
        f1=f2;
        f2=f3;
        f3=f1+f2;

    }

    cout << endl;

    return 0;
}

