#pragma once

#include <string>
#include "common.h"
#include "PadloElem.h"



class Hero
{
private:
	const std::string name;
	PadloElem* current_padloelem;
public:
	Hero(const std::string name);

	~Hero();

	void setCurrentPadloelem(PadloElem* padloelem);

	bool move(const MovingDirection& mozgasirany);
	

	void tamad();

	friend std::ostream& operator<<(std::ostream& os, const Hero& hero);
};

std::ostream& operator<<(std::ostream& os, const Hero& hero);