#pragma once

#include <fstream>

enum MovingDirection { ESZAK, KELET, NYUGAT, DEL };
enum UnitType {MONSTER, HERO, WALL};

struct Coordinate
{
	unsigned int x;
	unsigned int y;
};

std::ostream& operator<<(std::ostream& file, const Coordinate& coord);

