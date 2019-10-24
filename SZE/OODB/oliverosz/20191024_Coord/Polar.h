#pragma once
#include "Coord.h"

#include <cmath>

class Polar :
	public Coord
{
	double r, phi;
public:
	Polar(double r, double phi) : r(r), phi(phi)
	{}

	virtual double getX() const override { return r * cos(phi); }
	virtual double getY() const override { return r * sin(phi); }
	virtual double getR() const override { return r; }
	virtual double getPhi() const override { return phi; }

	virtual std::string toString() const {
		return "r=" + std::to_string(r) + " phi=" + std::to_string(phi);
	}

	virtual Polar& operator=(const Coord& other) {
		r = other.getR();
		phi = other.getPhi();
		return *this;
	}

	virtual Polar operator+(const Coord& other) const {
		return Polar(r + other.getR(), phi + other.getPhi());
	}
};

std::ostream& operator<<(std::ostream& o, const Polar& c);