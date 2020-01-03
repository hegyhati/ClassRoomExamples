#pragma once

#include "common.h"
#include <iostream>

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
	bool dead;
	UnitStat unitstat;
	PadloElem* current_padloelem;
	const UnitType unittype;
public:
	Unit(unsigned int health, unsigned int attack, unsigned int damage, unsigned int defense, const UnitType unittype): 
		unitstat({health, attack, damage, defense}),
		dead(false),
		current_padloelem(NULL),
		unittype(unittype)
	{}

	bool isKilled()
	{
		return unitstat.health == 0;
	}

	bool kill();
	

	bool move(MovingDirection movedir);
	void damage(unsigned int attack, unsigned int damage);

	void setCurrentPadloelem(PadloElem* padloelem);

	UnitType getUnitType() const
	{
		return unittype;
	}
};