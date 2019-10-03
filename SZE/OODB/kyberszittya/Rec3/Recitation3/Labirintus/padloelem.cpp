#include "Padloelem.h"

PadloElem::PadloElem() : PadloElem(0, 0)
{}

PadloElem::PadloElem(unsigned int x, unsigned int y) : coord({ x, y }), occupyingunit(NULL)
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


bool PadloElem::isFoglalt() const
{
	return occupyingunit != NULL;
}

void PadloElem::setOccupyingUnit(Unit* unit)
{
	occupyingunit = unit;
}

Coordinate PadloElem::getCoord() const
{
	return coord;
}