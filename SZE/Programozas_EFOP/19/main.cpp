/*
 * Feladat: Kerj be ket pozitiv egesz szamot: n, k.
 * Ird ki n alatta k-t.
 *
 * Peldak:
 * 5 2 -> 10
 * 5 5 -> 1
 * 5 0 -> 1
 * 
 */



#include<iostream>
using namespace std;

int factorial(int x){
    if (x==0) return 1;
    else return x*factorial(x-1);
}

int choose (int n, int k) {
    return factorial(n) / (factorial(k)*factorial(n-k));
}

int choose2 (int n, int k){
    if (n==k) return 1;
    else if (k==0) return 1;
    else return choose2(n-1,k)+choose2(n-1,k-1);
}

int main(){
    int n,k;
    cin >> n >> k;

    cout << choose2(n,k) << endl;

    return 0;
}

