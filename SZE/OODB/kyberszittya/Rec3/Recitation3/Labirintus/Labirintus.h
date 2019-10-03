#pragma once

#include "Hero.h"
#include "Padloelem.h"
#include "Szorny.h"
#include <iostream>

constexpr unsigned int LABIRINTUS_SIZE_X = 10;
constexpr unsigned int LABIRINTUS_SIZE_Y = 5;
constexpr unsigned int LABIRINTUS_PADLOELEMEK { LABIRINTUS_SIZE_X * LABIRINTUS_SIZE_Y };

class Labirintus
{
private:
	const int max_monster_cnt;
	Monster* monsters;
	PadloElem elems[LABIRINTUS_PADLOELEMEK];
	Hero& hero;
public:
	Labirintus(Hero& hero);
	Labirintus(Hero& hero, const int monster_cnt);
	~Labirintus();

	void print() const;

	/**
	Initialize neighbors of the labyrinth
	*/
	void initializeNeighbors();

	void initHeroPosition(const unsigned int x, const unsigned int y);

	void initMonsterPosition(const int monster_id, 
		const unsigned int x, const unsigned int y);
};