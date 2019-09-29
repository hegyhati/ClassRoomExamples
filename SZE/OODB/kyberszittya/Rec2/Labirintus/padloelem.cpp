#include "Padloelem.h"

PadloElem::PadloElem() : PadloElem(0, 0)
{}

PadloElem::PadloElem(unsigned int x, unsigned int y) : coord({ x, y }), foglalt(false)
{
	neighbors[MovingDirection::ESZAK] = NULL;
	neighbors[MovingDirection::KELET] = NULL;
	neighbors[MovingDirection::NYUGAT] = NULL;
	neighbors[MovingDirection::DEL] = NULL;
}

PadloElem* PadloElem::getNeighborElem(const MovingDirection& dir) const
{
	return neighbors[dir];
}

void PadloElem::setCoordinate(unsigned int x, unsigned int y)
{
	coord.x = x;
	coord.y = y;
}

void PadloElem::setNeighborElem(const MovingDirection& dir, PadloElem* p)
{
	neighbors[dir] = p;
}

void PadloElem::setFoglalt()
{
	foglalt = true;
}

void PadloElem::setFree()
{
	foglalt = false;
}

bool PadloElem::isFoglalt() const
{
	return foglalt;
}

Coordinate PadloElem::getCoord() const
{
	return coord;
}