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

bool Game::anyMonsterLeft(Monster * monsters[MTN]) const{
    for (int m=0;m<MTN;m++)
        if(monsters[m]!=NULL) return true;
    return false;
}

int Game::getNextMonsterSlot(Monster * monsters[MTN]) const {
    for (int m=0;m<MTN;m++)
        if(monsters[m]==NULL) return m;
    return -1;
}

bool Game::start(int rounds, int spawn, int maxMonster) {
    int round=0;
    Monster * monsters[MTN];
    for(int m=0; m<MTN;m++) monsters[m]=NULL;
    int attacked=0;
    while(attacked<=maxMonster && (round<rounds || anyMonsterLeft(monsters))){
        if(round<rounds) {
            int x,y,midx;
            for(int s=0;s<spawn;s++) {
                x=width;
                y=8; // fairly random number
                midx=getNextMonsterSlot(monsters);
                monsters[midx]=new Monster(x,y,2,10);                
            }
        }
        print(monsters);
        for(int t=0;t<TWN;t++) {
            if (towers[t]!=NULL) {
                for(int m=0;m<MTN;m++) {
                    if (monsters[m]!=NULL) {
                        if(towers[t]->distance(*monsters[m]) <= towers[t]->getRange()) {
                            if (monsters[m]->attack(towers[t]->getDamage())){
                                delete monsters[m];
                                monsters[m]=NULL;
                            }
                        }                                
                    }
                }
            }            
        }
        print(monsters);
        for(int m=0;m<MTN;m++) {
            if (monsters[m]!=NULL) {
                if(monsters[m]->move()){
                    delete monsters[m];
                    monsters[m]=NULL;
                    attacked++;
                }                                          
            }
        }
        print(monsters);
        round++;
    }
    if (attacked>maxMonster) {
        for(int m=0;m<MTN;m++) {
            if (monsters[m]!=NULL) {
                delete monsters[m];
                monsters[m]=NULL;                     
            }
        }
        return false;
    }
    return true;
};

bool Game::isTowerAt(int x, int y) const {
    for(int t=0; t<TWN; t++)
        if (towers[t]!=NULL)
            if (towers[t]->isPosition(x,y))
                return true;
    return false;
}
bool Game::isMonsterAt(Monster * monsters[MTN], int x, int y) const {
    for(int m=0; m<MTN; m++)
        if (monsters[m]!=NULL)
            if (monsters[m]->isPosition(x,y))
                return true;
    return false;
}

void Game::print(Monster * monsters[MTN]) const {
    cout<<"\n\n+";
    for(int w=0; w<width; w++)
        cout<<"-";
    cout<<"+\n";
    for(int h=0;h<height;h++){
        cout <<"|";
        for(int w=0; w<width; w++)
            if(isTowerAt(w,h)) cout<<"T";
            else if(isMonsterAt(monsters,w,h)) cout<<"M";
            else cout<<" ";
        cout<<"|\n";
    }
    cout<<"+";
    for(int w=0; w<width; w++)
        cout<<"-";
    cout<<"+\n";
}
