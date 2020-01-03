#include "Unit.h"
#include "Padloelem.h"

bool Unit::move(MovingDirection movedir)
{
	PadloElem* p = current_padloelem->getNeighborElem(movedir);
	if (p != NULL)
	{
		current_padloelem->setOccupyingUnit(NULL);
		setCurrentPadloelem(current_padloelem->getNeighborElem(movedir));
		return true;
	}
	else
	{
		return false;
	}
}

void Unit::setCurrentPadloelem(PadloElem* padloelem)
{
	current_padloelem = padloelem;
	current_padloelem->setOccupyingUnit(this);
}