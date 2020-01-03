#pragma once

#include "Hero.h"
#include "Padloelem.h"

#include <iostream>

constexpr unsigned int LABIRINTUS_SIZE_X = 10;
constexpr unsigned int LABIRINTUS_SIZE_Y = 5;
constexpr unsigned int LABIRINTUS_PADLOELEMEK { LABIRINTUS_SIZE_X * LABIRINTUS_SIZE_Y };

class Labirintus
{
private:
	PadloElem elems[LABIRINTUS_PADLOELEMEK];
	Hero& hero;
public:
	Labirintus(Hero& hero);

	void print() const;

	/**
	Initialize neighbors of the labyrinth
	*/
	void initializeNeighbors();

	void initHeroPosition(const unsigned int x, const unsigned int y);
};