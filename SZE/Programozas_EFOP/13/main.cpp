/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es ird ki az osztoit.
 * 
 *
 * Peldak:
 * 7 --> 1 7
 * 6 --> 1 2 3 6
 * 15 --> 1 3 5 15
 * 1 --> 1
 * 256 --> 1 2 4 8 16 32 64 128 256
 *
 */



#include<iostream>
using namespace std;

int main(){
    int n;

    do {
        cin >> n;
    } while (n<1);

    for (int i=1;i<=n;i++)
        if (n%i==0) cout<<i<<" ";

    cout << endl;

    return 0;
}

