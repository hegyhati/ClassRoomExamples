/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es ird ki hogy prim-e.
 * 
 *
 * Peldak:
 * 7 --> prim
 * 6 --> nem prim
 * 15 --> nem prim
 * 1 --> nem prim
 * 11 --> prim
 *
 */

bool isPrime(int n){
    int count=0;
    for(int i=1; i<=n; i++)
        if (!(n%i)) count++;
    return count==2;
}

bool isPrime2(int n){
    if (n==1) return false;
    for(int i=2; i*i <= n; i++)
        if(!(n%i)) return false;
    return true;
}


#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;

    if (isPrime(n)) cout << "Prim\n";
    else cout << "Nem prim\n";

    return 0;
}

