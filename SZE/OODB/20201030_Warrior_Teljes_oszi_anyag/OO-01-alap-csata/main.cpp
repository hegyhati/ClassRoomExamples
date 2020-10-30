#include <iostream>
using namespace std;

int main(){
  int hp1, dmg1, hp2, dmg2;
  cin >> hp1 >> dmg1 >> hp2 >> dmg2;

  while (hp1>0 && hp2>0) {
    cout << "HP: "<<hp1<<" DMG: "<<dmg1<<"   --->  HP: "<<hp2<<" DMG: "<<dmg2<<endl; 
    hp2-=dmg1; 
    if (hp2<0) hp2=0;
    if (hp2>0) {
      cout << "HP: "<<hp1<<" DMG: "<<dmg1<<"   <---  HP: "<<hp2<<" DMG: "<<dmg2<<endl;
      hp1-=dmg2;
      if (hp1<0) hp1=0;
    }
  }
  cout << "HP: "<<hp1<<" DMG: "<<dmg1<<"   ----  HP: "<<hp2<<" DMG: "<<dmg2<<endl;

  return 0;
}

/*
HP: 25 DMG: 3   --->  HP: 15 DMG: 8
HP: 25 DMG: 3   <---  HP: 12 DMG: 8
HP: 17 DMG: 3   --->  HP: 12 DMG: 8
HP: 17 DMG: 3   <---  HP:  9 DMG: 8
HP:  9 DMG: 3   --->  HP:  9 DMG: 8
HP:  9 DMG: 3   <---  HP:  6 DMG: 8
HP:  1 DMG: 3   --->  HP:  6 DMG: 8
HP:  1 DMG: 3   <---  HP:  3 DMG: 8
HP:  0 DMG: 3   --->  HP:  3 DMG: 8
*/
