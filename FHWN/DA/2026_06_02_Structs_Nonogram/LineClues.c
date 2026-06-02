#include "LineClues.h"

#include <stdlib.h>
#include <stdio.h>

// Assumes integers separated by single dash 
// Assumes string ending in \0
// Assumes at least 1 number
LineClues parseClues(const char* cluetext) {
    LineClues lcs;
    int count = 1;
    for (const char* pc = cluetext; *pc != '\0'; ++pc) 
        if (*pc == '-') ++count;
    lcs.size = count;
    lcs.clues = (int*) malloc(count * sizeof(int));
    int current_idx=0;
    int current_value=0;
    for (const char* pc = cluetext; *pc != '\0'; ++pc) {
        if  (*pc == '-') {
            lcs.clues[current_idx++] = current_value;
            current_value = 0;
        } else {
            current_value *= 10;
            current_value += *pc - '0';
        }
    }
    lcs.clues[current_idx] = current_value;
    return lcs;
}

void printClues(LineClues lcs) {
    for(int i = 0; i < lcs.size; ++i)
        printf(" %d", lcs.clues[i]);
    printf("\n");
}

void freeClues(LineClues* plcs) {
    plcs->size = 0;
    free(plcs->clues);
    plcs->clues = NULL;
}
