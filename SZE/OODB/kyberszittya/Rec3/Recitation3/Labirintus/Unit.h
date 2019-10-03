#pragma once

#include "common.h"

class PadloElem;

struct UnitStat
{
	unsigned int health;
	unsigned int attack;
	unsigned int damage;
	unsigned int defense;
};

class Unit
{
protected:
	UnitStat unitstat;
	PadloElem* current_padloelem;
public:
	Unit(unsigned int health, unsigned int attack, unsigned int damage, unsigned int defense): 
		unitstat({health, attack, damage, defense}),
		current_padloelem(NULL)
	{}

	bool isDead()
	{
		return unitstat.health == 0;
	}

	bool move(MovingDirection movedir);

	void setCurrentPadloelem(PadloElem* padloelem);
};