#pragma once

#include <string>

struct ProductQty {
	std::string name;
	int unitPrice;
	int quantity;

	std::string toString() const {
		return name + "\t" + std::to_string(unitPrice) + "\t" + std::to_string(quantity);
	}
};