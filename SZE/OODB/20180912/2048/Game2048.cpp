#include "Game2048.hpp"
#include <iostream>
#include <random>
#include <chrono>
#include <iomanip>

using namespace std;


  
class Position{
  public:
    int r;
    int c;
    Position(int r, int c):r(r),c(c){}
    bool good() const {return r>=0 && r<4 && c>=0 && c<4;}
    Position operator+ (char direction) const {
      switch(direction){
        case 'u': return Position(r-1,c);
        case 'd': return Position(r+1,c);
        case 'l': return Position(r,c-1);
        case 'r': return Position(r,c+1);
      }
      return Position(r,c);
    }
};

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



bool Game2048::move(int& from, int& to){
  if(to==EMPTY) {
    to=from;
    from=EMPTY;
    return true;
  } else return false;
}

bool Game2048::merge(int& from, int& to){
  if(from==to) {
    from=EMPTY;
    to*=2;
    return true;
  } else return false;
}

bool Game2048::shift(int r, int c, char direction){
  if(table[r][c]==EMPTY) return false;
  bool change=false;
  Position p(r,c);
  Position pn=p+direction;
  while(pn.good()){
    if (move(table[p.r][p.c],table[pn.r][pn.c])) {
      change = true;
      p=pn;
      pn=p+direction;
    } else break;
  }
  if(pn.good() && merge(table[p.r][p.c],table[pn.r][pn.c])) change=true;
  return change;
}

bool Game2048::shift(char direction){
  bool change=false;
  switch(direction){
    case 'u': 
      for(int r=1; r<4; r++) for (int c=0; c<4;c++) 
        if(shift(r,c,direction)) change=true; 
      break;
    case 'd': 
      for(int r=2; r>=0; r--) for (int c=0; c<4;c++)
        if(shift(r,c,direction)) change=true; 
      break;
    case 'l': 
      for(int c=1; c<4; c++) for (int r=0; r<4;r++) 
        if(shift(r,c,direction)) change=true; 
      break;
    case 'r': 
      for(int c=2; c>=0; c--) for (int r=0; r<4;r++)
        if(shift(r,c,direction)) change=true; 
      break;
  }
  return change;  
}

bool Game2048::win() const {
  for(int r=0;r<4;r++)
    for(int c=0;c<4;c++)
      if(table[r][c]>=2048) return true;
  return false;
}

void Game2048::play(){ 
  char dir;
  while(!gameover()){
    print();
    do {
      cout<<"Which direction?"<<endl;
      cin>>dir;
    } while(!shift(dir));
    insertnewrandom();
  }
  if(win()){
    cout<<"Yeeppeeeeeee!!!!"<<endl;
  } else {
    cout<<"Loser...."<<endl;
  }
}
