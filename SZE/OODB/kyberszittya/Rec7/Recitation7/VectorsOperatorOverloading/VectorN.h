#pragma once

#include <vector>

template<int N, typename T> class VectorN
{
private:
	std::vector<T> vals;
public:
	VectorN<N,T>() : vals(N) { }
	VectorN<N,T>(std::initializer_list<double> il) : vals(il) {}
	VectorN<N,T>(const VectorN<N,T>& other) : vals(other.vals)
	{}

	// Overload << operator
	template<int N0, typename T0> friend std::ostream& operator<<(std::ostream& os, VectorN<N0, T0>& v);

	template<int N0, typename T0> friend VectorN<N0,T0> operator+(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	template<int N0, typename T0> friend VectorN<N0,T0> operator-(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	template<int N0, typename T0> friend VectorN<N0,T0> operator*(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	template<int N0, typename T0> friend VectorN<N,T0> operator/(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	template<int N0, typename T0> friend bool operator==(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	template<int N0, typename T0> friend bool operator!=(const VectorN<N0,T0>& v0, const VectorN<N0,T0>& v1);
	// Overload index operator
	T& operator[](const int index)
	{
		return vals[index];
	}
	// Overload addition operator
	VectorN<N,T>& operator+=(const VectorN<N,T>& v)
	{
		for (unsigned int i = 0; i < N; i++)
		{
			vals[i] += v.vals[i];
			
		}
		
	}

};



template<int N0, typename T0> VectorN<N0, T0> operator+(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	VectorN<N0, T0> res;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] = v0.vals[i] + v1.vals[i];
	}
	
	return res;
}

template<int N0, typename T0> VectorN<N0, T0> operator-(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	VectorN<N0, T0> res;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] = v0.vals[i] - v1.vals[i];
	}

	return res;
}

template<int N0, typename T0> VectorN<N0, T0> operator*(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	VectorN<N0, T0> res;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] = v0.vals[i] * v1.vals[i];
	}

	return res;
}

template<int N0, typename T0> VectorN<N0, T0> operator/(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	VectorN<N0, T0> res;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] = v0.vals[i] / v1.vals[i];
	}

	return res;
}

template<int N0, typename T0> VectorN<N0, T0> operator==(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	bool res = true;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] &= v0.vals[i] == v1.vals[i];
		if (!res) {
			return false;
		}
	}

	return true;
}

template<int N0, typename T0> VectorN<N0, T0> operator!=(const VectorN<N0, T0>& v0, const VectorN<N0, T0>& v1)
{
	bool res = true;
	for (unsigned int i = 0; i < N0; i++)
	{
		res[i] &= v0.vals[i] == v1.vals[i];
		if (!res) {
			return true;
		}
	}

	return false;
}

template<int N0, typename T0> std::ostream& operator<<(std::ostream& os, VectorN<N0, T0>& v)
{
	for (unsigned int i = 0; i < N0; i++)
	{
		os << v[i] << ',';

	}
	return os;
}