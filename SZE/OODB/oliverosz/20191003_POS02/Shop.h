#pragma once

#include <string>

#include "Basket.h"
#include "ProductQty.h"

class Shop {
	ProductQty* inventory;
	int invSize;
	int income = 0;
	const std::string invFile;
	Basket basket;
public:
	Shop(const std::string& filename);
	~Shop();
	void printInventory() const;
	int getIncome() const { return 0; }

	bool addToBasket(std::string productName, int qty);
	bool removeFromBasket(std::string productName);
	void printBasket() const { basket.print(); }
	void clearBasket();
	void purchase();
};