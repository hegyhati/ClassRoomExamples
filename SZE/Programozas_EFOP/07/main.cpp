/*
 * Feladat: Kerjunk be egy egesz szamot, es irjuk ki addig a pozitiv egesz szamokat.
 * A szam bekereset addig ismeteljuk, amig pozitiv nem lesz.
 * 
 *
 * Peldak:
 * 5 -> 1 2 3 4 5
 * 0 3 -> 1 2 3
 *
 */

#include<iostream>
using namespace std;

int main(){
    int n;

    do {
        cin >> n;
    } while (n <= 0);

    
    for (int i=1;i<=n;i++)
        cout << i << " ";

    cout<<endl;
    
    return 0;
}

