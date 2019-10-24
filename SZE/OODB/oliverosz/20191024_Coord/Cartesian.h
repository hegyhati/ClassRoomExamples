#pragma once
#include "Coord.h"

#include <cmath>

class Cartesian :
	public Coord
{
	double x, y;
	friend std::ostream & operator<<(std::ostream&, const Cartesian&);
public:
	Cartesian(double x, double y) : x(x), y(y)
	{}

	virtual double getX() const override { return x; }
	virtual double getY() const override { return y; }
	virtual double getR() const override { return sqrt(x * x + y * y); }
	virtual double getPhi() const override { return atan2(y, x); }

	virtual std::string toString() const {
		return "x=" + std::to_string(x) + " y=" + std::to_string(y);
	}

	virtual Cartesian& operator=(const Coord& other) override {
		x = other.getX();
		y = other.getY();
		return *this;
	}

	virtual Cartesian operator+(const Coord& other) const {
		return Cartesian(x + other.getX(), y + other.getY());
	}
};

std::ostream& operator<<(std::ostream& o, const Cartesian& c);

Cartesian operator+(const Coord& c1, const Coord& c2);