#include "Game.hpp"
#include <string>
#include <iostream>
using namespace std;

int main(){
    Game testgame(50,10);
    string answer;
    int x, y;

    do {
        cout<<"Hova tegyem a tornyot, adj 0 0-t, hogyha tobbet nem akarsz.\t";
        cin>>x>>y;
        testgame.addTower(x,y);
        // test negative
        // test othertower
        // test budget
    } while(x!=0 || y!=0);

    if(testgame.start(5,1))
        cout<<"Grat, nyertel!\n";
    else
        cout<<"Majd legkozelebb.\n";
    
}
