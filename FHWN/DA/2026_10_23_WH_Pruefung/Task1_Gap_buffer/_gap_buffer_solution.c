#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define RESIZE_FACTOR 2

typedef struct {
    size_t capacity; // total capacity for characters
    size_t left;     // number of characters before the cursor = index of the next typed character (0 if nothing)
    size_t right;    // index where the content after the cursor starts (capacity if nothing)
    char* data;
} Gap_Buffer;

Gap_Buffer initialize_buffer(size_t size) {
    return (Gap_Buffer) {
        .capacity = size,
        .left = 0,
        .right = size,
        .data = (char*) malloc (size * sizeof(char))
    };
}

void free_buffer(Gap_Buffer* pgb) {
    pgb->capacity = pgb->left = pgb->right = 0;
    free(pgb->data);
    pgb->data = NULL;
}

void debug(Gap_Buffer* pgb) {
    fflush(stdout);
    for (size_t i = 0; i < pgb->capacity; ++i)
        putc( i < pgb->left || i >= pgb->right ? pgb->data[i] : '_', stdout);
    putc(' ', stdout);
    fwrite(pgb->data, sizeof(char), pgb->left, stdout);
    putc('|', stdout);
    fwrite(pgb->data + pgb->right, sizeof(char), pgb->capacity - pgb->right, stdout);
    putc('\n', stdout);
    fflush(stdout);
}

void resize(Gap_Buffer* pgb) {
    char* new_data = (char*) malloc(RESIZE_FACTOR*(pgb->capacity)*sizeof(char));
    memcpy(new_data, pgb->data, pgb->left);
    memcpy(new_data + (RESIZE_FACTOR-1) * pgb->capacity + pgb->right, pgb->data + pgb->right, pgb->capacity - pgb->right);
    free(pgb->data);
    pgb->data = new_data;
    pgb->right += (RESIZE_FACTOR-1)*pgb->capacity;
    pgb->capacity *= RESIZE_FACTOR;
}

void type(Gap_Buffer* pgb, char c) {
    pgb->data[pgb->left++] = c;
    if (pgb->left == pgb->right) resize(pgb);
}

void insert_text(Gap_Buffer* pgb, const char* text){
    for (size_t i = 0; i < strlen(text); ++i)
        type(pgb, text[i]);
}

void move_left(Gap_Buffer* pgb){
    if (pgb->left == 0) return;
    pgb->data[--(pgb->right)] = pgb->data[--(pgb->left)];
}

void move_right(Gap_Buffer* pgb){
    if (pgb->right == pgb->capacity) return;
    pgb->data[(pgb->left)++] = pgb->data[(pgb->right)++];
}

void backspace(Gap_Buffer* pgb){
    if (pgb->left == 0) return;
    --(pgb->left);
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