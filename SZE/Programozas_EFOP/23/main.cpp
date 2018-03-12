/*
 * Feladat: Kerj be ket pozitiv egesz szamot, ird ki a legnagyobb kozos osztojukat.
 * 
 *
 * Peldak:
 * 3 5 -> 1
 * 2 8 -> 2
 * 6 9 -> 3
 *
 */



#include<iostream>
using namespace std;

int& max(int& a, int& b) {return (a>b)?a:b;}
int& min(int& a, int& b) {return (b<a)?b:a;}

int gcd_simple(int a, int b){
    int gcd=min(a,b);
    while(a%gcd || b%gcd) gcd--;
    return gcd;
}

int gcd_euclides(int a, int b){
    while(a!=b) {
        cout<<a<<"\t"<<b<<endl;
        if(a>b) a-=b;
        else b-=a;
    }
    return a;
}

int gcd_euclides2(int a, int b){
    while(a!=b) {
        cout<<a<<"\t"<<b<<endl;
        max(a,b)-=min(a,b);
    }
    return a;
}

int main(){
    int a,b;
    cin >> a >> b;

    

    cout << "GCD("<<a<<","<<b<<")="<<gcd_euclides2(a,b)<<endl;

    return 0;
}

