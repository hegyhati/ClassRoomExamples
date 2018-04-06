/*
 * Feladat: Kerj be egy szamot, majd ird ki kettes szamrendszerben. 
 * 
 *
 * Peldak:
 * 3 -> 11
 * 2 -> 10
 * 65 -> 1000001
 * 37 -> 100101
 *
 */



#include<iostream>
using namespace std;

int main(){

    int n;
    cin >> n;
    int digits[1024];
    int x;
    

    for(x=0;n!=0;n/=2,x++) {
        digits[x] = n%2;
    }

    for(x--;x>=0;x--) cout << digits[x];
    
    cout << endl;

    return 0;
}

