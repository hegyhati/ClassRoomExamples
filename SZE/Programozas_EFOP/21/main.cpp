/*
 * Feladat: Kerj be egy pozitiv egesz szamot, es rajzold ki a Pascal haromszog paritasat ilyen melysegig az alabbi peldanak megfeleloen.
 * (Sierpinski haromszog)
 * 
 * Az elso ketto, szamokkal teli haromszog csak segitseg keppen van megadva, azt nem kell kiirni.
 *
 * Pelda:
 * 6
 *          
 *           1
 *         1   1
 *       1   2   1
 *     1   3   3   1
 *   1   4   6   4   1
 * 1   5   10  10  5   1
 *
 *           1
 *         1   1
 *       1   0   1
 *     1   1   1   1
 *   1   0   0   0   1
 * 1   1   0   0   1   1
 *
 *      XX
 *     XXXX
 *    XX  XX
 *   XXXXXXXX
 *  XX      XX
 * XXXX    XXXX
 * 
 */



#include<iostream>
using namespace std;

long int factorial(int n) {
    long int fact=1;
    for(int i=2;i<=n;i++) fact*=i;
    return fact;
}

long int choose(int n, int k) {
    return factorial(n) / (factorial(n-k)*factorial(k));
}


int choose2 (int n, int k){
    if (n==k) return 1;
    else if (k==0) return 1;
    else return choose2(n-1,k)+choose2(n-1,k-1);
}

int main(){

    int n;
    cin >> n;

    for(int row=0; row<n; row++){
        for(int s=0;s<n-row;s++) cout<<" ";
        for(int column=0; column<row+1; column++)
            cout << ((choose2(row,column)%2)?"XX":"  ");
        cout<<endl;
    }
    return 0;
}

