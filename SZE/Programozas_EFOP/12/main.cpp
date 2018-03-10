/*
 * Kerj be egy szamot.
 * Rajzolj ki egy ekkora magassagu haromszoget, piramist az alabbi peldanak megfeleloen.
 *
 * Pelda:
 * 
 * 5
 *
 *     X
 *    XXX
 *   XXXXX
 *  XXXXXXX
 * XXXXXXXXX
 *
 */

#include<iostream>
using namespace std;

int main(){
    int size;
    cin >> size;

    for(int row=0;row<size;row++){
        for(int s=0;s<size-1-row;s++)
            cout<<" ";
        for(int x=0;x<1+2*row;x++)
            cout<<"X";
        cout<<endl;
    }


    return 0;
}

