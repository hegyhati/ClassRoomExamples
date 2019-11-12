#include "Music.h"

#include <iostream>

std::string Music::toString() const
{
    return artist + " - " + title + " (" + lengthStr() + ')';
}

void Music::print() const
{
    std::cout << toString() << "\n";
}
