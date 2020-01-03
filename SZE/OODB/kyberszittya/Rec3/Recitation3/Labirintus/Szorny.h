#pragma once

#include "Unit.h"

class Monster : public Unit
{
private:
public:
	Monster() : Unit({100, 10, 12, 5}) 
	{}

	void damage(unsigned int attack, unsigned int damage)
	{
		unitstat.health -= ((double)(unitstat.defense) / (double)(unitstat.attack)) * damage;
	}

	

};