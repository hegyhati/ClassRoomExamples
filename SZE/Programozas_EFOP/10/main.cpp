/*
 * Feladat: Kerj be egy karaktert, es ket szamot: a, b.
 * a-rol es b-rol feltetelezhetjuk, hogy pozitiv egeszek.
 * Rajzolj ki egy a x b meretu teglalapot a bekert karakterbol ugy, hogy a kozepet szokozokkel toltsd fel.
 * Feltetelezhetjuk a-rol es b-rol is, hogy legalabb 3.
 *
 * Pelda:
 * 
 * X 4 5
 *
 * XXXX
 * X  X
 * X  X
 * X  X
 * XXXX
 *
 */

#include<iostream>
using namespace std;

void fullRow(int width, char c){
    for(int w=0;w<width;w++)
        cout<<c;
    cout << endl;
}

void middleRow(int width, char c){
    cout << c;
    for(int w=0;w<width-2;w++)
        cout<<" ";
    cout << c << endl;
}

int main(){
    char c;
    int width, height;
    cin >> c >> width >> height;

    fullRow(width,c);

    for(int h=0;h<height-2;h++)
        middleRow(width,c);

    fullRow(width,c);


    return 0;
}

