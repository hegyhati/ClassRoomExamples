#include "Sphere.h"

Sphere::Sphere(const double r) : r(r) {};
const double Sphere::volume() {
	return 4 / 3 * pi*r*r*r;
};

const bool Sphere::isValid() {
	return r > 0 ? true : false;
}