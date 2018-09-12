#include "Game2048.hpp"
#include <iostream>
using namespace std;

void Game2048::insertnewrandom(int number){
  // TODO do real random later
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      if(table[r][c]==EMPTY) {
        table[r][c]=number;
        return;
      }
}


Game2048::Game2048(){
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      table[r][c]=EMPTY;
  insertnewrandom();
  insertnewrandom(4);
}


bool Game2048::gameover() const {
  // TODO real gameover
  bool isfull=true;
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      if(table[r][c]==EMPTY)
        isfull=false;
  return isfull;
}

void Game2048::print() const{
  for(int r=0;r<4;r++){
    for(int c=0;c<4;c++)
      if(table[r][c]==EMPTY) cout<<".";
      else cout<<table[r][c];
    cout<<endl;
  }
}

void Game2048::up() {}
void Game2048::down() {
  for(int r=2;r>=0;r--){
    for(int c=0;c<4;c++){
      int rnew=r+1;
      if(table[rnew][c]==EMPTY) {
        while(table[rnew+1][c]==EMPTY && rnew<3) rnew++;
        table[rnew][c]=table[r][c];
        table[r][c]=EMPTY;
      }
    }
  }
  insertnewrandom();
}


void Game2048::left() {}
void Game2048::right() {}
bool Game2048::win() const {return true;}
