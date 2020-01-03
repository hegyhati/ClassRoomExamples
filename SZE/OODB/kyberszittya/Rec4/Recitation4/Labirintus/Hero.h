#pragma once

#include <string>
#include "common.h"
#include "Unit.h"




class Hero: public Unit
{
private:
	const std::string name;
public:
	Hero(const std::string name, unsigned int health, unsigned int attack, unsigned int damage, unsigned int defense);

	~Hero();

	
	friend std::ostream& operator<<(std::ostream& os, const Hero& hero);
};

std::ostream& operator<<(std::ostream& os, const Hero& hero);