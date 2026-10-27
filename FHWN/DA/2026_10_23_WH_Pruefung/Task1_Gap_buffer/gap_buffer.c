#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define RESIZE_FACTOR 2

typedef struct {
    // TODO
} Gap_Buffer;

Gap_Buffer initialize_buffer(size_t size) {
    // TODO
}

void free_buffer(Gap_Buffer* pgb) {
    // TODO
}

void debug(Gap_Buffer* pgb) {
    // TODO 
}

void type(Gap_Buffer* pgb, char c) {
    // TODO - must be O(1) -- aggregated
}

void insert_text(Gap_Buffer* pgb, const char* text){
    for (size_t i = 0; i < strlen(text); ++i)
        type(pgb, text[i]);
}

void move_left(Gap_Buffer* pgb){
    // TODO - must be O(1)
}

void move_right(Gap_Buffer* pgb){
    // TODO - must be O(1)
}

void backspace(Gap_Buffer* pgb){
    // TODO - must be O(1)
}

int main() {
    Gap_Buffer gb = initialize_buffer(10);
    insert_text(&gb, "This!");
    debug(&gb);
    move_left(&gb);
    debug(&gb);
    insert_text(&gb, " is a ni");
    debug(&gb);
    insert_text(&gb, "ce Rap buffer");
    debug(&gb);
    for (int i = 0; i<9; ++i) {
        move_left(&gb);
        debug(&gb);
    }
    backspace(&gb);
    type(&gb,'G');
    for (int i = 0; i<10; ++i) {
        move_right(&gb);
        debug(&gb);
    }
    insert_text(&gb, " ;-) ");   
    debug(&gb);

    free_buffer(&gb);
    return 0;
}