#include "Polar.h"

std::ostream & operator<<(std::ostream & o, const Polar & c)
{
	return std::cout << "r=" << c.getR() << " phi=" << c.getPhi();
}
