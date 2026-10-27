## Motivation

We really like the bunny from the previous exercise, so we decided to make a real life iron statue of it by welding together the triangle plates as they are in the model. 

Unfortunately, iron can get rusty, and [Rust tends to spread](https://commandlinux.com/statistics/rust-programming-language-adoption/). 

If a triangle gets rusty, by the next day all its neighbors (those triangles with whom it shares an edge) will also get rusty. 

Write a `main` that asks for the index of a triangle in the model, and then:
 - prints out how many days does the bunny need to get completely rusty if that selected triangle gets rusty first.
 - for each day, print out how many new triangles did get rusty.

## Bonus point exercise 1 

Let `main` print out first, which is the luckiest and unluckiest triangle to be "Patient 0", and how many days are needed in their case.

## Bonus point exercise 2

The logic for spreading is different: the time needed for rust to spread from a triangle to another is a linear function of the distance between their centroids. Print out the order in which the triangles get rusty for the starting triangle provided by the user. 

## Code 

Feel free to reuse any datastructure or utility functions from Task 2.