#include "Cube.h"

bool Cube::validCube() const
{
	if (a > 0.0 && b > 0.0 && c > 0.0)
	{
		return true;
	}
	return false;
}

double Cube::volume() const
{
	return a * b * c;
}

Cube::Cube(const double a, const double b, const double c) :
	a(a), b(b), c(c)
{

}