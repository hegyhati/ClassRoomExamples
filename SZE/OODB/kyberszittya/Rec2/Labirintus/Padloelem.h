#pragma once

#include "common.h"

class PadloElem
{
private:
	Coordinate coord;
	bool foglalt;

	PadloElem* neighbors[4];
public:
	PadloElem(unsigned int x, unsigned int y);

	PadloElem();

	PadloElem* getNeighborElem(const MovingDirection& dir) const;

	void setCoordinate(unsigned int x, unsigned int y);

	void setNeighborElem(const MovingDirection& dir, PadloElem* p);

	void setFoglalt();

	void setFree();

	bool isFoglalt() const;

	Coordinate getCoord() const;
};