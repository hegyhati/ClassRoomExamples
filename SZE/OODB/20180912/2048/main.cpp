#include <iostream>
#include "Game2048.hpp"
using namespace std;

int main(){
  Game2048 test;
  char dir;
  while(! test.gameover()){
    test.print();
    cout<<"Which direction?"<<endl;
    cin>>dir;
    switch(dir){
      case 'u': test.up();break;
      case 'd': test.down();break;      
      case 'l': test.left();break;      
      case 'r': test.right();break;
    }
  }
  if(test.win()){
    cout<<"Yeeppeeeeeee!!!!"<<endl;
  } else {
    cout<<"Loser...."<<endl;
  }
}
