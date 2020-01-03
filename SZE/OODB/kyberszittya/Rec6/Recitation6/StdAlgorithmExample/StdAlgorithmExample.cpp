// StdAlgorithmExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
	std::vector<double> vals({ 0.1, 0.8, 0.4, 1, 2.9, 5.3, 4.1, 
		1.9, 10.3, 4.7, 5.2 });
	std::vector<double> vals;
	
	std::cout << "Original list: ";
	for (const auto& v : vals)
	{
		std::cout << v << ' ';
	}
	std::cout << '\n';
	// Revert
	std::cout << "Reversed list: ";
	std::reverse(std::begin(vals), std::end(vals));
	for (const auto& v : vals)
	{
		std::cout << v << ' ';
	}
	std::cout << '\n';
	// Max
	auto max_el = std::max_element(vals.begin(), vals.end());
	std::cout << "Max element: " << 
		vals[std::distance(vals.begin(), max_el)] << '\n';
	// Binary search
	if (std::binary_search(vals.begin(), vals.end(), 10.3)) {
		std::cout << "Found element\n";
	}
	else
	{
		std::cout << "Element not found\n";
	}
	// Sort
	std::sort(vals.begin(), vals.end());
	std::cout << "Sorted list: ";
	for (const auto& v : vals)
	{
		std::cout << v << ' ';
	}
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
