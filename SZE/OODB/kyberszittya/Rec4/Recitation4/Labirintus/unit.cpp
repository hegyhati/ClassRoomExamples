#include "Unit.h"
#include "Padloelem.h"

#include <iostream>

bool Unit::move(MovingDirection movedir)
{
	PadloElem* p = current_padloelem->getNeighborElem(movedir);
	if (p != NULL)
	{
		if (!p->isFoglalt())
		{
			current_padloelem->setOccupyingUnit(NULL);
			setCurrentPadloelem(current_padloelem->getNeighborElem(movedir));
			return true;
		}
		else if (p->getOccupyingUnit()->getUnitType() != UnitType::OBSTACLE)
		{
			p->getOccupyingUnit()->damage(this->unitstat.attack, this->unitstat.damage);
			std::cout << "Attacking monster" << std::endl;
			return true;
		}
	}
	else
	{
		return false;
	}
}

void Unit::damage(unsigned int attack, unsigned int damage)
{
	unsigned int dmg = (unsigned int)(((double)(unitstat.defense) / (double)(unitstat.attack)) * damage);
	if (unitstat.health <= dmg)
	{
		unitstat.health = 0;
		kill();
	}
	else
	{
		unitstat.health -= (unsigned int)(((double)(unitstat.defense) / (double)(unitstat.attack)) * damage);
	}	
	std::cout << unitstat.health << std::endl;
}

void Unit::setCurrentPadloelem(PadloElem* padloelem)
{
	current_padloelem = padloelem;
	current_padloelem->setOccupyingUnit(this);
}

bool Unit::kill()
{
	if (isKilled())
	{
		std::cout << "DEAD" << std::endl;
		if (!dead)
		{
			
			current_padloelem->setOccupyingUnit(NULL);
			current_padloelem = NULL;
			dead = true;
		}
		return true;
	}
	return false;
}