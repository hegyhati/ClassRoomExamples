#pragma once

constexpr double pi = 3.14;

class Sphere
{
private:
	double r;
public:
	Sphere(const double r);
	const double volume();
	const bool isValid();
};