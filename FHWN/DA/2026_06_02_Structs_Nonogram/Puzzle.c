#include "Puzzle.h"

#include <stdlib.h>
#include <stdio.h>

Puzzle loadPuzzle(const char* filename) {
    FILE* f = fopen(filename,"r");
    char buffer[100];
    Puzzle p;
    fscanf(f, "%d x %d", &p.row_count, &p.col_count);
    p.row_clues = (LineClues*) malloc(p.row_count * sizeof(LineClues));
    p.col_clues = (LineClues*) malloc(p.col_count * sizeof(LineClues));

    for (int r = 0; r < p.row_count; ++r) {
        fscanf(f, "%s", buffer);
        p.row_clues[r] = parseClues(buffer);
    }
       for (int c = 0; c < p.col_count; ++c) {
        fscanf(f, "%s", buffer);
        p.col_clues[c] = parseClues(buffer);
    }
    fclose(f);
    return p;
}

void printPuzzle(Puzzle p) {
    printf("\n--- %d by %d Puzzle ---\n\n", p.row_count, p.col_count);
    printf("\nRow clues:\n");
    for (int r = 0; r < p.row_count; ++r) {
        printf(" - Row %d: ", r+1);
        printClues(p.row_clues[r]);
    }
    printf("\nColumn clues:\n");
    for (int c = 0; c < p.col_count; ++c) {
        printf(" - Column %d: ", c+1);
        printClues(p.col_clues[c]);
    }
}

void freePuzzle(Puzzle* pp) {
    for (int r = 0; r < pp->row_count; ++r) 
        freeClues(pp->row_clues + r);
    for (int c = 0; c < pp->col_count; ++c) 
        freeClues(pp->col_clues + c);
    pp->row_count = 0;
    pp->col_count = 0;
    free(pp->row_clues);
    free(pp->col_clues);
    pp->row_clues = NULL;
    pp->col_clues = NULL;
}


