#ifndef GAME2048_HPP
#define GAME2048_HPP

#define EMPTY 0

class Game2048 {
      
    int table[4][4];

    void insertnewrandom();
    
    bool move(int& from, int& to);
    bool merge(int& from, int& to);
    
    bool shift(char direction);
    bool shift(int r, int c, char direction);
    
    bool gameover() const; 
    void print() const;
    bool win() const;
    
  public:
  
    Game2048(); 
    void play();
};

#endif

