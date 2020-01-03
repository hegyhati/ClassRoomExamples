// FunctorExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

#include <random>

template<class F> void apply(std::vector<int>& vec, F func)
{
	for (unsigned int i = 0; i < vec.size(); i++)
	{
		vec[i] = func(vec[i]);
	}
}

class TransformerObject
{
private:
	int val;
public:
	TransformerObject(int val) : val(val) {}
	int operator()(int x)
	{
		return val * std::exp2(std::sqrt(x));
	}
};

int main()
{
	std::random_device rnd_device;
	std::mt19937 mersenne_engine{ rnd_device() };  // Generates random integers
	std::uniform_int_distribution<int> dist{ 1, 52 };

	std::vector<int> vec(20);
	auto gen = [&dist, &mersenne_engine]() {
		return dist(mersenne_engine);
	};
	std::generate(std::begin(vec), std::end(vec), gen);

	for (const auto& v : vec)
	{
		std::cout << v << ' ';
	}
	std::cout << '\n';

	auto sqr = [](int vec) {
		return vec * vec;
	};

	apply(vec, sqr);
	for (const auto& v : vec)
	{
		std::cout << v << ' ';
	}
	std::cout << '\n';
	auto modulus95 = [](int vec) {
		return vec % 95;
	};
	apply(vec, modulus95);
	for (const auto& v : vec)
	{
		std::cout << v << ' ';
	}	
	std::cout << '\n';
	// Apply transformer object
	TransformerObject transformerobject(-3);
	apply(vec, transformerobject);
	for (const auto& v : vec)
	{
		std::cout << v << ' ';
	}
	std::cout << '\n';
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
