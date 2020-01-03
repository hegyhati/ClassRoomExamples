#include "common.h"

std::ostream& operator<<(std::ostream& file, const Coordinate& coord)
{
	file << '(' << coord.x << ',' << coord.y << ')';
	return file;
}