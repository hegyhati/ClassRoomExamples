#include "Hero.h"

Hero::Hero(const std::string name)
	:
	name(name),
	current_padloelem(NULL)
{}

Hero::~Hero()
{
	current_padloelem = NULL;
}

void Hero::setCurrentPadloelem(PadloElem* padloelem)
{
	current_padloelem = padloelem;
}

bool Hero::move(const MovingDirection& mozgasirany)
{

	PadloElem* p = current_padloelem->getNeighborElem(mozgasirany);
	if (p != NULL)
	{
		current_padloelem->setFree();
		setCurrentPadloelem(current_padloelem->getNeighborElem(mozgasirany));
		current_padloelem->setFoglalt();
		return true;
	}
	else
	{
		return false;
	}


}

void Hero::tamad()
{

}

std::ostream& operator<<(std::ostream& os, const Hero& hero)
{
	//os << hero.name << hero.current_padloelem->getCoord();
	return os;
}