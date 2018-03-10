/*
 * Feladat: Kerj be egy pozitiv egesz szamot.
 * Ird ki a faktorialisat.
 * 
 *
 * Peldak:
 * 3 -> 6
 * 5 -> 120
 *
 */

#include<iostream>
using namespace std;

int factorial(int n) {
    int fact = 1;
    for(int i=1; i<=n;i++)
        fact*=i;
    return fact;
}


int factorial_recursive(int n) {
    if(n==0) return 1; 
    else return n*factorial_recursive(n-1);
}

int main(){
    int n;
    cin >> n;

    
    cout << factorial_recursive(n) << endl;

    return 0;
}

