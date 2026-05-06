# Notes

## 2nd exam

In the 2nd programming exam: 
 - You will not be sorting simple integers/floats, but some structs.
 - The data will probably come from a file.
 - The problem will not be "write a X-sort". There will be a "story" (real life setting) for the problem. 
 - You may have to implement a sorting algorithm, that we learned. Or a slight variation of it. Or another algorithm, that has something to do with sorting. 
 - Error handling will never be in focus, i.e., you can assume, that the file exists, and properly formatted, etc.
 - But segfaults, memory leaks are still serious mistakes.

## Exercises

These exercises are more complex than the ones we had at the end of classes. 
If you haven't yet implemented **ALL** sorting algorithms on simple `int` arrays, I strongly suggest you to do that, and then come back here.
Some of the exercises exceed what can be expected in the exam, but they are good practice exercises nonetheless.

### 00/01 - Array struct

The goal of this is to get more confident with structs, pointers, pointers to structs, etc. Nothing sorting specific. More like a warm-up. 

00 is more easy to understand version.
In 01 the functions always expect a pointer to the struct as a first argument.
This looks more convoluted, but the signatures are more consistent, and this actually gets really close to the `this` / `self` behavior of OO languages.

You can go one step further by renaming `Array` to `_Array` and typedefing `_Array *` as `Array`, and having only pointers in `main` too. 

In the second test you will definitely not need to go this far with structs, but later...

### 02/03 - Rectangles

The exercise from last week. The goal is to first encounter a situation, where it is not only integers/floats that need sorting, and maybe we sort by two different values. 
Practice the sorting algorithm, you have the most issues with.

In 03 the comparing logic is not baked in into the function but provided as a function pointer. This is something that again will not appear in the 2nd test, but reflects "real practice".

### 04 - Shell sort

We step back from structs for a second, the goal here is to practice implementing a variant of a learned sorting algorithm. 
In this case: Insertion sort "variant": Shell sort. 
You can use one of the `Array` structs done in 00/01, or start with simple `int*` first.

### 05 - Bookings

This exercise has multiple goals:
 - we get back to sorting structs
 - for the first time, there is a "story", and you have to understand the relation between real life things and code
 - a new algorithm is provided, explained in steps (but the first step is sorting, that's why it is here)

Moreover, `main` cannot be touched, and nothing (no function signatures) are given, you have to plan them yourself.

But, the scheduling algorithm is not specified, you may chose arbitrary, but again, I recommend something "uncomfortable" for practice purposes.

An example input file, and python script that can generate such input files is also provided.

## 06/07 - Zombies

Story, structs, primary queue with a heap. 
For help, some signatures, code snippets are given. 
Doing stuff like `move` has nothing to do with AlgoDat, but it is good programming practice, so I left it as a todo.

This is definitely way more in quantity than something for the 2nd Test.
But again... good practice.

Extension ideas for more practice:
 - zombies have health, and cannon does a random damage from an interval.
 - all of the zombies move at once (not really once, but all move between two shots. tricky to maintain the heap property).
 - We have two cannons, one shoots at the closest, the other one shoots at the one with the lowest health. (heaps of pointers, but it gets tricky again.)





