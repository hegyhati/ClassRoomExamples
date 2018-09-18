#ifndef GAME2048_HPP
#define GAME2048_HPP

#define EMPTY 0

class Game2048 {
    int table[4][4];

    void insertnewrandom();
    bool moveormerge(int& from, int& to);
  public:
    Game2048(); // 1: fixen 2: random
    bool gameover() const; //1: tele van-e 2: van-e jo lepes
    void print() const;
    void up(); // 1. fixen az ujat 2: random
    void down();
    void left();
    void right();
    bool win() const;
};

#endif

