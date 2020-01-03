#include "Hero.h"
#include "Padloelem.h"

Hero::Hero(const std::string name, unsigned int health, unsigned int attack, unsigned int damage, unsigned int defense)
	:
	Unit(health, attack, damage, defense),
	name(name)
{}

Hero::~Hero()
{
	current_padloelem = NULL;
}






std::ostream& operator<<(std::ostream& os, const Hero& hero)
{
	os << hero.name << hero.current_padloelem->getCoord();
	return os;
}