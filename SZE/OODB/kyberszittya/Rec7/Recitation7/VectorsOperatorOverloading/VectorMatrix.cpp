#include "VectorMatrix.h"


std::ostream& operator<<(std::ostream& os, const Vector3<double>& v)
{
	os << v.vals[0] << ',' << v.vals[1] << ',' << v.vals[2];
	return os;
}

std::ostream& operator<<(std::ostream& os, const Matrix3<double>& v)
{
	os << v.vals[0] << ',' << v.vals[1] << ',' << v.vals[2] << '\n';
	os << v.vals[3] << ',' << v.vals[4] << ',' << v.vals[5] << '\n';
	os << v.vals[6] << ',' << v.vals[7] << ',' << v.vals[8] << '\n';
	return os;
}

