#include <stdio.h>
#include "GameState.h"

int main(int argc, char** argv) {
    GameState my_game = newGame(argv[1]);
    printGameState(my_game);
    freeGameState(&my_game);    
    return 0;
}