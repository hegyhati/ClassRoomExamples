// CustomIteratorExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <iterator>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

template<int N, class T> class BlockingArray
{
private:
	std::vector<T> data;
	int current_elements;
public:
	BlockingArray() : current_elements(0) { data.reserve(N); }
	BlockingArray(std::initializer_list<T> il) : data(il), current_elements(il.size()) {}

	void push(T elem)
	{
		if (current_elements < N)
		{
			data.push_back(elem);
			current_elements++;
		}
		else
		{
			throw std::length_error("Array is full");
		}
	}

	T pop()
	{
		current_elements--;
		T res = data.back();
		data.pop_back();
		return res;
	}

	struct iterator
	{
		typename std::vector<T>::iterator t;
	
		iterator& operator++()
		{
			++t;
			return *this;
		}

		bool operator==(iterator other) const
		{
			return t == other.t;
		}
		bool operator!=(iterator other) const
		{
			return !(*this==other);
		}

		using iterator_category = std::forward_iterator_tag;
		using difference_type = std::ptrdiff_t;
		using value_type = T;
		
		using pointer = T*;
		T& operator*() { return *t; }
			 
	};
	iterator begin() { return { std::begin(data) }; }
	iterator end() { return { std::end(data) }; }
};

void blockingArray()
{
	BlockingArray<5, double> blocking_array;
	try
	{
		blocking_array.push(10.8);
		blocking_array.push(20.0);
		blocking_array.push(15.0);
		blocking_array.push(16.25);
		blocking_array.push(17.1);
		blocking_array.push(18.0);

	}
	catch (std::length_error& en)
	{
		std::cerr << en.what() << '\n';
	}
	blocking_array.pop();
	blocking_array.pop();
	for (const auto& v : blocking_array)
	{
		std::cout << v << '\n';
	}
}

int main()
{
	blockingArray();
	_CrtDumpMemoryLeaks();
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
