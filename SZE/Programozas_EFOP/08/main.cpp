/*
 * Feladat: Kerjunk be ket egesz szamot, es irjuk ki a koztuk levo egesz szamokat novekvo sorrendben. 
 *
 * Peldak:
 * 1 5 -> 1 2 3 4 5
 * 0 3 -> 0 1 2 3
 * -3 2 -> -3 -2 -1 0 1 2
 * 8 2 -> 2 3 4 5 6 7 8
 * 5 5 -> 5
 *
 */



#include<iostream>
using namespace std;

int main(){
    int a,b;
    cin >> a >> b;

    int smaller = a < b ? a : b;
    int larger  = a >= b ? a : b;

    for(int i=smaller;i<=larger;i++)
        cout << i << " ";

    cout << endl;
    
    return 0;
}

