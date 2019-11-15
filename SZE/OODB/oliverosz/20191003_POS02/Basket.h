#pragma once

#include "ProductQty.h"

class Basket {
	ProductQty* contents;
	int count=0, size=0;
public:
	Basket();
	Basket(const Basket& other);
	~Basket();
	Basket& operator=(const Basket& other);
	void add(const ProductQty& toAdd);
	int remove(const std::string& productName);
	void print() const;
};
