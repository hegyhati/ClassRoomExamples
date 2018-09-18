#include "Game2048.hpp"
#include <iostream>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;

void Game2048::insertnewrandom(){
  unsigned seed = static_cast<int> (chrono::system_clock::now().time_since_epoch().count());
  default_random_engine generator(seed);
  uniform_int_distribution<int> distribution(0,3);
  int start_row = distribution(generator);
  int start_column = distribution(generator); 
  int number=2*(1+distribution(generator)/2);
  
  for(int r=start_row;r<start_row+4;r++)
    for(int c=start_column;c<start_column+4;c++)
      if(table[r%4][c%4]==EMPTY) {
        table[r%4][c%4]=number;
        return;
      }
}


Game2048::Game2048(){
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      table[r][c]=EMPTY;
  insertnewrandom();
  insertnewrandom();
}


bool Game2048::gameover() const {
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      if(
        table[r][c]==EMPTY
        || (r!=0 && table[r-1][c]==table[r][c]) 
        || (c!=0 && table[r][c-1]==table[r][c])
      ) return false;
  return true;
}

void Game2048::print() const{
  cout<<"+"; for(int c=0;c<4;c++) cout <<"-----+";cout<<endl;
  for(int r=0;r<4;r++){
    cout<<"|"; for(int c=0;c<4;c++) cout <<"     |";cout<<endl;
    cout<<"|";
    for(int c=0;c<4;c++){
      if(table[r][c]==EMPTY) cout<<"     |";
      else cout<<setw(4)<<table[r][c]<<" |";
    }
    cout<<endl;
    cout<<"|"; for(int c=0;c<4;c++) cout <<"     |";cout<<endl;
    cout<<"+"; for(int c=0;c<4;c++) cout <<"-----+";cout<<endl;
  }
}



bool Game2048::moveormerge(int& from, int& to){
  if(to==EMPTY) {
    to=from;
    from=EMPTY;
    return true;
  } else if (from == to) {
    from=EMPTY;
    to*=2;
    return false;
  } else {
    return false;
  }
}

void Game2048::up() { // TODO: check if a move really changes something
  for(int r=1;r<4;r++){
    for(int c=0;c<4;c++){
      if(table[r][c]!=EMPTY) {
        for(int m=0; r-m-1>=0 && moveormerge(table[r-m][c],table[r-m-1][c]); m++);
      }
    }
  }
  insertnewrandom();
}

void Game2048::down() {
  for(int r=2;r>=0;r--){
    for(int c=0;c<4;c++){
      if(table[r][c]!=EMPTY) {
        for(int m=0; r+m+1<4 && moveormerge(table[r+m][c],table[r+m+1][c]); m++);
      }
    }
  }
  insertnewrandom();
}


void Game2048::left() {
  for(int c=1;c<4;c++){
    for(int r=0;r<4;r++){
      if(table[r][c]!=EMPTY) {
        for(int m=0; c-m-1>=0 && moveormerge(table[r][c-m],table[r][c-m-1]); m++);
      }
    }
  }
  insertnewrandom();
}

void Game2048::right() {
  for(int c=2;c>=0;c--){
    for(int r=0;r<4;r++){
      if(table[r][c]!=EMPTY) {
        for(int m=0; c+m+1<4 && moveormerge(table[r][c+m],table[r][c+m+1]); m++);
      }
    }
  }
  insertnewrandom();
}


bool Game2048::win() const {
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      if(table[r][c]>=2048) return true;
  return false;
}
