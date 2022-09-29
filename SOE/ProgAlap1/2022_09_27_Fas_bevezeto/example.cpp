#include <iostream>
using namespace std;

int main() {
    unsigned int x,y;    
    cin >> x >> y;
    while (x>0) {
        if (x==y){
            cout << "Osztoja";
            return 0;
        } else {
            x = x - y;
        }
    }
    cout << "Nem osztoja";
}

/*

Beker: x
Beker: y
Amig x > 0:
	Ha x = y Akkor Kiir: osztoja, VEGE
	Kulonben: x = x – y
Kiir: nem osztoja, VEGE

*/