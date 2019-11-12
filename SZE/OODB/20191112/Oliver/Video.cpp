#include "Video.h"

#include <iostream>

std::string Video::toString() const
{
    return title + " (" + lengthStr() + " - " + std::to_string(width) + " x " + std::to_string(height) + ")";
}

void Video::print() const
{
    std::cout << toString() << "\n";
}
