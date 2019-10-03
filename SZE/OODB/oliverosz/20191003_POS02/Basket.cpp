#include "Basket.h"

#include <iostream>

using namespace std;

const int initialSize = 3;

Basket::Basket() :
	contents(new ProductQty[initialSize]),
	size(initialSize)
{
}

Basket::Basket(const Basket& other) :
	contents(new ProductQty[other.size]),
	count(other.count),
	size(other.size)
{
	for (int i = 0; i < count; ++i)
		contents[i] = other.contents[i];
	cout << "**Basket copy constructor**\n";
}

Basket & Basket::operator=(const Basket & other)
{
	if (size < other.count) {
		delete[] contents;
		contents = new ProductQty[other.size];
		size = other.size;
	}
	count = other.count;
	for (int i = 0; i < count; ++i)
		contents[i] = other.contents[i];
	cout << "**Basket assignment operator**\n";
	return *this;
}

Basket::~Basket()
{
	delete[] contents;
}

void Basket::add(const ProductQty& toAdd)
{
	int i = 0;
	while (i < count && contents[i].name != toAdd.name)
		++i;
	if (i < count) {
		contents[i].quantity += toAdd.quantity;
		return;
	}
	if (count == size) { // array is full, increase size
		ProductQty* newBasket = new ProductQty[2 * size];
		for (int i = 0; i < count; ++i)
			newBasket[i] = contents[i];
		delete[] contents;
		contents = newBasket;
		size *= 2;
	}
	contents[count] = toAdd;
	++count;
}

int Basket::remove(const std::string & productName)
{
	// search productName
	int i = 0;
	while (i < count && contents[i].name != productName)
		++i;
	if (i < count) {
		// remove element and shift others from higher index
		int qty = contents[i].quantity;
		while (i+1 < count) {
			contents[i] = contents[i + 1];
			++i;
		}
		count--;
		return qty;
	}
	return 0;
}

void Basket::print() const
{
	cout << "Basket contents:\n";
	for (int i=0; i<count; ++i)
		cout << contents[i].toString() << endl;
}
