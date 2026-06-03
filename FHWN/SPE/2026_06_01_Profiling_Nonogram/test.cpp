#include "nonogram.h"
#include <iostream>

int main(int argc, char** argv) {
    Line l(argv[1]);
    Clue c(argv[2]);
    std::cout << l.deduce(c).toSring() << std::endl;
}