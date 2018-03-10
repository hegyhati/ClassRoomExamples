/*
 * Feladat:
 * Kerj be ket szamot, a-t es n-t, majd ird ki a^n-t.
 * Feltetelezheto, hogy n egesz szam.
 *
 * Pelda:
 *  2   3   --->    8
 *  3   2   --->    9
 *  -3  2   --->    9
 *  5   -1  --->    0.2
 *  42  0   --->    1
 *  0.5 2   --->    0.25
 *
 */



#include<iostream>
using namespace std;

int main(){
    double a;
    int n;

    cin >> a;
    cin >> n;

    double an = 1;

     
    for (int i=0;i<n;i++) {
        an *= a;
    }

    cout << an << endl;
    

    return 0;
}

