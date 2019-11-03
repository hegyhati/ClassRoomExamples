#pragma once

#include "Vector3.h"

template<class T> class Matrix3
{
private:
	std::vector<T> vals;
public:
	Matrix3<T>() : vals(9) {}
	Matrix3<T>(std::initializer_list<T> il) : vals(il) {}
	Matrix3<T>(const Matrix3& other) : vals(other.vals) {}
	// Overload operator<<
	friend std::ostream& operator<<(std::ostream& os, const Matrix3<T>& v);
	// Overload arithmetics
	template<typename T0> friend Matrix3<T0> operator+(const Matrix3<T0>& m0, const Matrix3<T0>& m1);
	template<typename T0> friend Matrix3<T0> operator*(const Matrix3<T0>& m0, const Matrix3<T0>& m1);
	template<typename T0> friend Vector3<T0> operator*(const Matrix3<T0>& m0, Vector3<T0>& v);
};

template<typename T0> Matrix3<T0> operator+(const Matrix3<T0>& m0, const Matrix3<T0>& m1)
{
	Matrix3<T0> res(m0);
	res.vals[0] += m1.vals[0];
	res.vals[1] += m1.vals[1];
	res.vals[2] += m1.vals[2];
	res.vals[3] += m1.vals[3];
	res.vals[4] += m1.vals[4];
	res.vals[5] += m1.vals[5];
	res.vals[6] += m1.vals[6];
	res.vals[7] += m1.vals[7];
	res.vals[8] += m1.vals[8];
	return res;
}

template<typename T0> Matrix3<T0> operator*(const Matrix3<T0>& m0, const Matrix3<T0>& m1)
{
	Matrix3<T0> res;
	res.vals[0] = m0.vals[0] * m1.vals[0] + m0.vals[1] * m1.vals[3] + m0.vals[2] * m1.vals[6];
	res.vals[1] = m0.vals[0] * m1.vals[1] + m0.vals[1] * m1.vals[4] + m0.vals[2] * m1.vals[7];
	res.vals[2] = m0.vals[0] * m1.vals[2] + m0.vals[1] * m1.vals[5] + m0.vals[2] * m1.vals[8];

	res.vals[3] = m0.vals[3] * m1.vals[0] + m0.vals[4] * m1.vals[3] + m0.vals[5] * m1.vals[6];
	res.vals[4] = m0.vals[3] * m1.vals[1] + m0.vals[4] * m1.vals[4] + m0.vals[5] * m1.vals[7];
	res.vals[5] = m0.vals[3] * m1.vals[2] + m0.vals[4] * m1.vals[5] + m0.vals[5] * m1.vals[8];

	res.vals[6] = m0.vals[6] * m1.vals[0] + m0.vals[7] * m1.vals[3] + m0.vals[8] * m1.vals[6];
	res.vals[7] = m0.vals[6] * m1.vals[1] + m0.vals[7] * m1.vals[4] + m0.vals[8] * m1.vals[7];
	res.vals[8] = m0.vals[6] * m1.vals[2] + m0.vals[7] * m1.vals[5] + m0.vals[8] * m1.vals[8];

	return res;
}

template<typename T0> Vector3<T0> operator*(const Matrix3<T0>& m0, Vector3<T0>& v1)
{
	Vector3<T0> res{
		m0.vals[0] * v1[0] + m0.vals[1] * v1[1] + m0.vals[2] * v1[2],
		m0.vals[3] * v1[0] + m0.vals[4] * v1[1] + m0.vals[5] * v1[2],
		m0.vals[6] * v1[0] + m0.vals[7] * v1[1] + m0.vals[8] * v1[2]
	};
	return res;
}

template<class T> class RotationYaw : public Matrix3<T>
{
public:
	RotationYaw<T>(T yaw) : Matrix3<T>({
		cos(yaw),  sin(yaw), 0,
		-sin(yaw), cos(yaw), 0,
		0, 0, 1
		}) {}
};