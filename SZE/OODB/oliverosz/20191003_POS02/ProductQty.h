#pragma once

#include <string>

struct ProductQty {
	std::string name;
	int unitPrice;
	int quantity;

	std::string toString() const {
		return name + "\t" + std::to_string(unitPrice) + "\t" + std::to_string(quantity);
	}

	//bool operator==(const std::string&);
	bool operator==(const ProductQty& other) {
		return name == other.name && unitPrice == other.unitPrice && quantity == other.quantity;
	}
};

bool operator==(const ProductQty&, const std::string&);