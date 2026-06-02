#ifndef PUZZLE_H
#define PUZZLE_H

#include "LineClues.h"

typedef struct {
    int row_count;
    int col_count;
    LineClues* row_clues;
    LineClues* col_clues;
} Puzzle;

Puzzle loadPuzzle(const char* filename);
void printPuzzle(Puzzle p);
void freePuzzle(Puzzle* pp);

#endif