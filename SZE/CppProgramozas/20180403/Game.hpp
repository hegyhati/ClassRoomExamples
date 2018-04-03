#ifndef GAME_HPP
#define GAME_HPP

#define TWN 1024
#define MTN 1024

#include "Tower.hpp"
#include "Monster.hpp"

#include <iostream>

class Game{
    private:
        int width;
        int height;
        Tower * towers[TWN];

        int getNextTowerIndex() const;
        bool isTowerAt(int x, int y) const;
        bool isMonsterAt(Monster * monsters[MTN], int x, int y) const;
        bool anyMonsterLeft(Monster * monsters[MTN]) const;
        int getNextMonsterSlot(Monster * monsters[MTN]) const;

    public:
        Game(int width, int height);
        ~Game();
        void addTower(int x, int y);
        bool start(int rounds, int spawn, int maxMonster=0);
        void print(Monster * monsters[MTN]) const;
    
};

#endif
