#include "Coord.h"

#include "Cartesian.h"
#include "Polar.h"

std::ostream& operator<<(std::ostream& o, const Coord& c) {
	//return o << c.toString();
	// if toString() wouldn't exist
	try {
		return o << dynamic_cast<const Cartesian&>(c);
	}
	catch (std::exception e) {
	}
	try {
		return o << dynamic_cast<const Polar&>(c);
	}
	catch (std::exception e) {
	}
	return o;
}


