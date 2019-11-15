#include "Cartesian.h"

std::ostream & operator<<(std::ostream & o, const Cartesian & c)
{
	return std::cout << "x=" << c.x << " y=" << c.y;
}

Cartesian operator+(const Coord & c1, const Coord & c2)
{
	return Cartesian(c1.getX() + c2.getX(), c1.getY() + c2.getY());
}
