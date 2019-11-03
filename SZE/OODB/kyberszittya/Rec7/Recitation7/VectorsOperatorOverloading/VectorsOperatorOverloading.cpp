// VectorsOperatorOverloading.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "VectorMatrix.h"

// WARNING: this is just a representation of operator overloading.
// For performance matrix calculations, use Eigen/GLM/MKL etc.




int main()
{
	Vector3<double> v({ 0.4, 0.6, 0.3 });
	Vector3<double> v0({ 0.1, 0.3, 0.7 });

    std::cout << v << '\n';
	std::cout << v0 << '\n';
	std::cout << v + v0 << '\n';
	std::cout << v - v0 << '\n';
	std::cout << v * v0 << '\n';
	std::cout << v / v0 << '\n';
	std::cout << (v == v0) << '\n';
	std::cout << (v == v) << '\n';
	std::cout << (v != v) << '\n';
	std::cout << v[0] << '\n';
	// Matrix3
	Matrix3<double> m({1.0, 2.3, 4.5, 
		6.7, 8.9, 1.2,
		5.6, 7.8, 2.4});
	std::cout << m << '\n';
	std::cout << m * v << '\n';
	std::cout << dotproduct(v0, v) << '\n';
	VectorN<5, double> vec0({ 1.0, 2.0, 3.0, 4.0, 5.0 });
	VectorN<5, double> vec1({ 1.0, 2.0, 3.0, 4.0, 5.0 });
	std::cout << vec0 << '\n';
	auto n = vec0 + vec1;
	std::cout << n << '\n';
	RotationYaw<double> yaw0(0.12566);
	std::cout << yaw0 << '\n';
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
