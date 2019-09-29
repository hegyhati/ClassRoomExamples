#pragma once

// Kiszámítjuk a kocka térfogatát
class Cube
{
private:
	const double a, b, c;
public:

	Cube(const double a, const double b, const double c);

	// Számoljunk térfogatot!
	double volume() const;
	// Ellenõrizzük, jó-e a kocka
	bool validCube() const;
};