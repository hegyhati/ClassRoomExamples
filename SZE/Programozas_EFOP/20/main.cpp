/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es ird ki a Pascal haromszoget ilyem melysegben a lenti pelda szerint.
 *
 * Pelda:
 * 6
 *
 * 1  1  1  1  1  1
 * 1  2  3  4  5
 * 1  3  6  10
 * 1  4  10
 * 1  5
 * 1
 * 
 */



#include<iostream>
#include<iomanip>
using namespace std;


int Pascal(int row, int column){
    if (row==0 || column==0) return 1;
    return Pascal(row,column-1) + Pascal(row-1,column);
}

int main(){
    int n;
    cin >> n;
    for(int row=0;row<n;row++) {
        for (int column=0;column<n-row;column++)
            cout << setw(4) << Pascal(row,column);
        cout << endl;
    }
    return 0;
}

