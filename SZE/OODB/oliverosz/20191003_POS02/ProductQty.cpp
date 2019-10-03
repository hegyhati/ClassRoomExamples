#include "ProductQty.h"

bool operator==(const ProductQty &prod, const std::string &name)
{
	return prod.name == name;
}
