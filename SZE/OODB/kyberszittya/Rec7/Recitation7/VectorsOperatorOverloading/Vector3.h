#pragma once

#include <iostream>
#include <initializer_list>
#include <vector>


template<typename T> class Vector3
{
private:
	std::vector<T> vals;
public:
	Vector3<T>() : vals(3) { }
	Vector3<T>(std::initializer_list<double> il) : vals(il) {}
	Vector3<T>(const Vector3<T>& other) : vals(other.vals)
	{}

	// Overload << operator
	friend std::ostream& operator<<(std::ostream& os, const Vector3<T>& v);

	template<typename T0> friend Vector3<T0> operator+(const Vector3<T0>& v0, const Vector3<T0>& v1);
	template<typename T0> friend Vector3<T0> operator-(const Vector3<T0>& v0, const Vector3<T0>& v1);
	template<typename T0> friend Vector3<T0> operator*(const Vector3<T0>& v0, const Vector3<T0>& v1);
	template<typename T0> friend Vector3<T0> operator/(const Vector3<T0>& v0, const Vector3<T0>& v1);
	template<typename T0> friend bool operator==(const Vector3<T0>& v0, const Vector3<T0>& v1);
	template<typename T0> friend bool operator!=(const Vector3<T0>& v0, const Vector3<T0>& v1);
	// Overload index operator
	T& operator[](const int index)
	{
		return vals[index];
	}
	// Overload addition operator
	Vector3<T>& operator+=(const Vector3<T>& v)
	{
		vals[0] += v.vals[0];
		vals[1] += v.vals[1];
		vals[2] += v.vals[2];
	}

	template<typename T0> friend T0 dotproduct(Vector3<T0>& v0, Vector3<T0>& v1);
	
};

template<typename T0> T0 dotproduct(Vector3<T0>& v0, Vector3<T0>& v1)
{
	return v0[0] * v1[0] + v0[1] * v1[1] + v0[2] * v1[2];
}

template<typename T0> Vector3<T0> operator+(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	Vector3<T0> res({ v0.vals[0] + v1.vals[0], v0.vals[1] + v1.vals[1], v0.vals[2] + v1.vals[2] });
	return res;
}

template<typename T0> Vector3<T0> operator-(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	Vector3<T0> res({ v0.vals[0] - v1.vals[0], v0.vals[1] - v1.vals[1], v0.vals[2] - v1.vals[2] });
	return res;
}

template<typename T0> Vector3<T0> operator*(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	Vector3<T0> res({ v0.vals[0] * v1.vals[0], v0.vals[1] * v1.vals[1], v0.vals[2] * v1.vals[2] });
	return res;
}

template<typename T0> Vector3<T0> operator/(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	Vector3<T0> res({ v0.vals[0] / v1.vals[0], v0.vals[1] / v1.vals[1], v0.vals[2] / v1.vals[2] });
	return res;
}

template<typename T0> bool operator==(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	return (v0.vals[0] == v1.vals[0]) && (v0.vals[1] == v1.vals[1]) && (v0.vals[2] == v1.vals[2]);
}

template<typename T0> bool operator!=(const Vector3<T0>& v0, const Vector3<T0>& v1)
{
	return (v0.vals[0] != v1.vals[0]) && (v0.vals[1] != v1.vals[1]) && (v0.vals[2] != v1.vals[2]);
}