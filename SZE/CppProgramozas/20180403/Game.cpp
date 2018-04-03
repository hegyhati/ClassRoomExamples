#include "Game.hpp"
#include <iostream>
using namespace std;

Game::Game(int width, int height)
    : width(width), height(height){
    for (int i=0;i<TWN;i++)
        towers[i]=NULL;
}

Game::~Game() {
    for (int i=0;i<TWN;i++)
        if(towers[i] != NULL) {
            delete towers[i];
            towers[i]=NULL;
        }
}

int Game::getNextTowerIndex() const {
    int idx=0;
    while (towers[idx]!=NULL) idx++;
    return idx;
    // todo: range check
}

void Game::addTower(int x, int y){
    int idx=getNextTowerIndex();
    towers[idx]=new Tower(x,y,1,3);
}

bool Game::start(int rounds, int spawn, int maxMonster) {
    print();
    return true;
};

bool Game::isTowerAt(int x, int y) const {
    for(int t=0; t<TWN; t++)
        if (towers[t]!=NULL)
            if (towers[t]->isPosition(x,y))
                return true;
    return false;
}

void Game::print() const {
    cout<<"\n\n+";
    for(int w=0; w<width; w++)
        cout<<"-";
    cout<<"+\n";
    for(int h=0;h<height;h++){
        cout <<"|";
        for(int w=0; w<width; w++)
            if(isTowerAt(w,h)) cout<<"T";
            else cout<<" ";
        cout<<"|\n";
    }
    cout<<"+";
    for(int w=0; w<width; w++)
        cout<<"-";
    cout<<"+\n";
}
