#include "Labirintus.h"

Labirintus::Labirintus(Hero& hero) : Labirintus(hero, 0, 0)
{

}

Labirintus::Labirintus(Hero& hero, const int monster_cnt, const int obstacle_cnt) :
	max_monster_cnt(monster_cnt), hero(hero)
{
	monsters = new Monster[monster_cnt];
	wallelems = new Fal[obstacle_cnt];
	current_monster_cnt = max_monster_cnt;
}

Labirintus::~Labirintus()
{
	delete[] monsters;
	delete[] wallelems;
}

void Labirintus::print() const
{
	for (unsigned int x = 0; x < LABIRINTUS_SIZE_X; x++)
	{
		std::cout << "-";
	}
	std::cout << "\n";
	for (unsigned int y = 0; y < LABIRINTUS_SIZE_Y; y++)
	{
		for (unsigned int x = 0; x < LABIRINTUS_SIZE_X; x++)
		{
			if (elems[y * LABIRINTUS_SIZE_X + x].isFoglalt())
			{
				switch (elems[y * LABIRINTUS_SIZE_X + x].getOccupyingUnit()->getUnitType())
				{
				case UnitType::HERO: {
					std::cout << 'O';
					break;
				}
				case UnitType::MONSTER: {
					std::cout << 'X';
					break;
				}
				case UnitType::OBSTACLE: {
					std::cout << 'H';
					break;
				}
				}
			}
			else
			{
				std::cout << " ";
			}
		}
		std::cout << '\n';
	}
	for (unsigned int x = 0; x < LABIRINTUS_SIZE_X; x++)
	{
		std::cout << "-";
	}
	std::cout << "\n";
}



void Labirintus::initializeNeighbors()
{
	// Y coord
	for (unsigned int y = 0; y < LABIRINTUS_SIZE_Y; y++)
	{
		// X coord
		for (unsigned int x = 0; x < LABIRINTUS_SIZE_X; x++)
		{
			elems[y * LABIRINTUS_SIZE_X + x].setCoordinate(x, y);
			// Left boundary
			if (x == 0)
			{
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(KELET, &elems[y * LABIRINTUS_SIZE_X + x + 1]);      // Point to east
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(DEL, &elems[(y + 1) * LABIRINTUS_SIZE_X + x]);    // Point to south					
				// Not in left-upper corner
				if (y > 0)
				{
					elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(ESZAK, &elems[(y - 1) * LABIRINTUS_SIZE_X + x]);    // Point to north
				}
			}
			// Right boundary
			else if (x == LABIRINTUS_SIZE_X - 1)
			{
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(NYUGAT, &elems[y * LABIRINTUS_SIZE_X + x - 1]);      // Point to west
				if (y < LABIRINTUS_SIZE_Y - 1)
				{
					elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(DEL, &elems[(y + 1) * LABIRINTUS_SIZE_X + x]);    // Point to south					
				}
				// Not in right-upper corner
				if (y > 0)
				{
					elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(ESZAK, &elems[(y - 1) * LABIRINTUS_SIZE_X + x]);    // Point to north
				}
			}
			else if (y == 0)
			{
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(KELET, &elems[y * LABIRINTUS_SIZE_X + x + 1]);      // Point to east
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(NYUGAT, &elems[y * LABIRINTUS_SIZE_X + x - 1]);      // Point to west
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(DEL, &elems[(y + 1) * LABIRINTUS_SIZE_X + x]);      // Point to south
			}
			else if (y == LABIRINTUS_SIZE_Y - 1)
			{
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(KELET, &elems[y * LABIRINTUS_SIZE_X + x + 1]);      // Point to east
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(NYUGAT, &elems[y * LABIRINTUS_SIZE_X + x - 1]);      // Point to west
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(ESZAK, &elems[(y - 1) * LABIRINTUS_SIZE_X + x]);      // Point to north
			}
			else
			{
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(KELET, &elems[y * LABIRINTUS_SIZE_X + x + 1]);
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(NYUGAT, &elems[y * LABIRINTUS_SIZE_X + x - 1]);
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(ESZAK, &elems[(y - 1) * LABIRINTUS_SIZE_X + x]);
				elems[y * LABIRINTUS_SIZE_X + x].setNeighborElem(DEL, &elems[(y + 1) * LABIRINTUS_SIZE_X + x]);
			}
		}
	}
}

bool Labirintus::noLivingMonsters()
{
	unsigned int living_monsters = 0;
	for (int i = 0; i < max_monster_cnt; i++)
	{
		if (!monsters[i].isKilled())
		{
			living_monsters++;
		}
	}
	return living_monsters==0;
}

void Labirintus::initHeroPosition(const unsigned int x, const unsigned int y)
{
	elems[y * LABIRINTUS_SIZE_X + x].setOccupyingUnit(&hero);
	hero.setCurrentPadloelem(&elems[y * LABIRINTUS_SIZE_X + x]);
}

void Labirintus::initMonsterPosition(const int monster_id, const unsigned int x, const unsigned int y)
{
	elems[y * LABIRINTUS_SIZE_X + x].setOccupyingUnit(&monsters[monster_id]);
	monsters[monster_id].setCurrentPadloelem(&elems[y * LABIRINTUS_SIZE_X + x]);
}

void Labirintus::initWallPosition(const int wall_id, const unsigned int x, const unsigned int y)
{
	elems[y * LABIRINTUS_SIZE_X + x].setOccupyingUnit(&wallelems[wall_id]);
	wallelems[wall_id].setCurrentPadloelem(&elems[y * LABIRINTUS_SIZE_X + x]);
}