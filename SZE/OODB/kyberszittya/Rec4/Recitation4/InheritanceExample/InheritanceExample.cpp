// InheritanceExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>
#include <string>

constexpr double PI = 3.14;

struct Position
{
	double x;
	double y;

	Position(double x, double y) : x(x), y(y) {}
};

std::ostream& operator<<(std::ostream& os, const Position& pos)
{
	os << '(' << pos.x << pos.y << ')';
	return os;
}

class Shape
{
private:
	
protected:
	Position position;
public:
	Shape(Position position): position(position)
	{

	}

	double getCircumfere() const
	{
		return 0.0;
	}

	double getArea() const
	{
		return 0.0;
	}

	Position getPosition() const
	{
		return position;
	}
};

std::ostream& operator<<(std::ostream& os, const Shape& shape)
{
	os << shape.getPosition() << ' ' << shape.getArea() << ' ' << shape.getCircumfere();
	return os;
}

class Circle : public Shape
{
private:
	const double radius;
public:
	Circle(const Position position, const double radius): Shape(position), radius(radius)
	{

	}

	double getArea() const
	{
		return radius * radius * PI;
	}

	double getCircumfere() const
	{
		return 2 * radius * PI;
	}
};

class Rectangle : public Shape
{
private:
	double a;
	double b;
public:
	Rectangle(const Position position, const double a, const double b) : Shape(position), a(a), b(b)
	{

	}

	double getArea() const
	{
		return a * b;
	}

	double getCircumfere() const
	{
		return 2 * (a + b);
	}
};

class Triangle : public Shape
{
private:
	double a;
	double b;
	double c;
public:
	Triangle(const Position position, const double a, const double b, const double c) : Shape(position), a(a), b(b), c(c)
	{

	}

	double getArea() const
	{
		double s = (a + b + c) / 2.0;
		return sqrt(s*(s - a) * (s - b) * (s - c));
	}

	double getCircumfere() const
	{
		return a + b + c;
	}
};

int main()
{
	Position p0({ 1.0, 2.0 });
	Circle c(p0, 1.0);
	std::cout << c << '\n';
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
