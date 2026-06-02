#include "GameState.h"

#include <stdlib.h>
#include <stdio.h>

GameState newGame(const char* filename) {
    GameState gs;
    gs.puzzle = loadPuzzle(filename);
    printPuzzle(gs.puzzle);
    gs.matrix = (State**) malloc( gs.puzzle.row_count * sizeof(State*));
    for (int r = 0; r < gs.puzzle.row_count; ++r) {
        gs.matrix[r] = (State*) malloc( gs.puzzle.col_count * sizeof(State));
        for (int c = 0; c < gs.puzzle.col_count; ++c) 
            gs.matrix[r][c] = UNKNOWN;
    }
    return gs;
}

void printGameState(GameState gs) {
    printPuzzle(gs.puzzle);
    printf("\n\n GAMESTATE \n\n");
    for (int r = 0; r < gs.puzzle.row_count; ++r) {
        for (int c = 0; c < gs.puzzle.col_count; ++c)   
            printf("%c",gs.matrix[r][c]);
        printf("\n");
    }
}

void freeGameState(GameState* pgs) {
    for (int r = 0; r < pgs->puzzle.row_count; ++r) 
        free(pgs->matrix[r]);
    free(pgs->matrix);
    pgs->matrix = NULL;
    freePuzzle(&(pgs->puzzle));
}
