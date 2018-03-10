/*
 * Feladat: Kerj be harom szamot: x0, dx, n.
 * Ird ki az x0 kezdetu, dx differenciaju, n elemu szamtani sorozatot.
 * 
 *
 * Peldak:
 * 1 2 3 -> 1 3 5
 * 10 5 6 -> 10 15 20 25 30 35
 * 1.2 0.3 2 -> 1.2 1.5
 * 1 -1 4 -> 1 0 -1 -2
 * 1 42 1 -> 1
 * 23 25 0 -> 
 *
 */



#include<iostream>
using namespace std;

int main(){
    double x0, dx;
    int n;
    cin >> x0 >> dx >> n;

    for(int i=0;i<n;i++)
        cout<<x0+i*dx<<" ";

    cout << endl;

    return 0;
}

