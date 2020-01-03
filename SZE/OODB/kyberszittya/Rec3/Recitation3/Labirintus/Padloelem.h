#pragma once

#include "common.h"
#include "Unit.h"

class PadloElem
{
private:
	Coordinate coord;
	Unit* occupyingunit;

	PadloElem* neighbors[4];
protected:

public:
	PadloElem(unsigned int x, unsigned int y);

	PadloElem();

	PadloElem* getNeighborElem(const MovingDirection& dir) const;

	void setCoordinate(unsigned int x, unsigned int y);

	void setNeighborElem(const MovingDirection& dir, PadloElem* p);

	void setOccupyingUnit(Unit* unit);

	bool isFoglalt() const;

	Coordinate getCoord() const;
};