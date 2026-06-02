#ifndef LINECLUES_H
#define LINECLUES_H

typedef struct {
    int* clues;
    int size;
} LineClues;

LineClues parseClues(const char* cluetext);
void printClues(LineClues lcs);
void freeClues(LineClues* plcs);

#endif
