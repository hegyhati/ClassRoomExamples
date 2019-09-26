#include "Basket.h"

#include <iostream>

using namespace std;

const int initialSize = 3;

Basket::Basket() :
	contents(new ProductQty[initialSize]),
	size(initialSize)
{
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

void Basket::print() const
{
	cout << "Basket contents:\n";
	for (int i=0; i<count; ++i)
		cout << contents[i].toString() << endl;
}
