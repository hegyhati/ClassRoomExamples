#include "Shop.h"

#include <fstream>
#include <iostream>

using namespace std;

Shop::Shop(const string& filename)
	: invSize(0), invFile(filename)
{
	ifstream input(filename);
	while (!input.eof()) {
		string name;
		input >> name;
		int price, qty;
		input >> price >> qty;
		if (name.empty())
			break;
		//cout << name << '\t' << price << '\t' << qty << endl;
		ProductQty* newInventory = new ProductQty[invSize + 1];
		for (int i = 0; i < invSize; i++)
			newInventory[i] = inventory[i];
		newInventory[invSize] = { name, price, qty };
		delete[] inventory;
		inventory = newInventory;
		++invSize;
	}
	// sort();
}

Shop::~Shop()
{
	ofstream out(invFile);
	if (!out.is_open()) {
		cerr << "Could not open inventory file " << invFile << " for writing.\n";
	}
	else {
		for (int i = 0; i < invSize; i++) {
			out << inventory[i].toString() << endl;
		}
	}
	delete[] inventory;
}

void Shop::printInventory() const
{
	for (int i = 0; i < invSize; i++) {
		cout << inventory[i].toString() << endl;
	}
}

bool Shop::addToBasket(const std::string& productName, int qty)
{
	// could be binary search if sort() is implemented
	int i = 0;
	while (i < invSize && !(inventory[i] == productName))
		++i;
	if (i < invSize) { // product found
		if (inventory[i].quantity < qty)
			return false;
		inventory[i].quantity -= qty;
		ProductQty toAdd = { inventory[i].name, inventory[i].unitPrice, qty };
		basket.add(toAdd);
		return true;
	}
	return false;
}

bool Shop::removeFromBasket(const std::string& productName)
{
	// try to remove product from basket
	int quantity = basket.remove(productName);
	// if successful, increase inventory
	if (quantity > 0) {
		int i = 0;
		while (i < invSize && inventory[i].name != productName)
			++i;
		if (i < invSize) {
			inventory[i].quantity += quantity;
		}
		return true;
	}
	return false;
}
