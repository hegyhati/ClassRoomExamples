#include <iostream>
#include <iomanip>
#include <string>

unsigned int pascal_bad(const unsigned int row, const unsigned int col) {
    return pascal_bad(row - 1, col) + pascal_bad(row - 1, col - 1);
}

unsigned int pascal_ok(const unsigned int row, const unsigned int col) {
    if (row == col || col == 0) return 1;
    return pascal_ok(row - 1, col) + pascal_ok(row - 1, col - 1);
}

void sierpinsky (const unsigned int depth) {
    for (unsigned int row = 0; row < depth; ++row) {
        std::cout << std::setw(depth - row) << "";
        for (unsigned int col = 0; col <= row; ++col) {
            std::cout << (pascal_ok(row, col) % 2 ? "XX" : "  ");
        }
        std::cout << "\n";
    }
}

void sierpinsky_fast(const unsigned int depth) {
    unsigned int cache[depth+1];
    for (unsigned int row = 0; row < depth; ++row) {
        cache[depth-row] = 1;
        std::cout << std::setw(depth - row) << ""; 
        if (row) std::cout << "XX"; 
        for(unsigned int column = depth - row + 1; column < depth; ++column) {
            cache[column] = cache[column] + cache[column+1];
            std::cout << (cache[column]  % 2 ? "XX" : "  "); 
        }
        std::cout << "XX\n";
    }
}


int main(int argc, char** argv) {
    const std::string method(argv[1]);
    const int depth = atoi(argv[2]);

    if (method == "recursive") sierpinsky(depth);
    else if (method == "dynamic") sierpinsky_fast(depth);

    return 0;
}