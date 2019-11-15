#pragma once
#include <string>
#include <iostream>

class Coord
{
public:
	virtual double getX() const = 0;
	virtual double getY() const = 0;
	virtual double getR() const = 0;
	virtual double getPhi() const = 0;

	virtual std::string toString() const = 0;

	std::string toLongString() const;

	virtual Coord& operator=(const Coord& other) = 0;
};

inline std::string Coord::toLongString() const {
	return "x=" + std::to_string(getX()) + " y=" + std::to_string(getY())
		+ " r=" + std::to_string(getR()) + " phi=" + std::to_string(getPhi());
}

std::ostream& operator<<(std::ostream& o, const Coord& c);
