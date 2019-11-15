#pragma once

#include "ProductQty.h"

class Basket {
	ProductQty* contents;
	int count=0, size=0;
public:
	Basket();
	~Basket();
	void add(const ProductQty& toAdd);
	void print() const;
};

