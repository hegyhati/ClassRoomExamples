/*
 * Feladat: Kerj be egy szamot,  majd egy masikat ami megadja, hogy az elso szamot milyen szamrendszerben ird ki.
 * A masodik szamrol feltetelezheto, hogy 2 es 9 kozotti.
 * 
 *
 * Peldak:
 * 3 5 -> 3
 * 8 2 -> 1000
 * 9 6 -> 13
 *
 */



#include<iostream>
#include<iomanip>
using namespace std;

int main(){

    int n;
    cin >> n;
    int m;
    cin >> m;

    int digits[128];
    int x;

    for(x=0;n!=0;n/=m,x++) {
        cout << setw(8)<<n << " | " << n%m << endl;
        digits[x]=n%m;
    }
    cout << setw(8) << n << endl << endl;
    
    for(x--;x>=0;x--)
        cout << digits[x];

    cout << endl;
    
    return 0;
}

