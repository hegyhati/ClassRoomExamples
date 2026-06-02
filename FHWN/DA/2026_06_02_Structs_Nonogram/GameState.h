#ifndef GAMESTATE_H
#define GAMESTATE_H

#include "Puzzle.h"

typedef enum {UNKNOWN = '?', FILLED = '#', EMPTY = ' '} State;

typedef struct {
    Puzzle puzzle;
    State** matrix; // [row][col] indexing
} GameState;

GameState newGame(const char* filename);
void printGameState(GameState gs);
void freeGameState(GameState* pgs);

#endif


