#include "Labirintus.h"

Labirintus::Labirintus(Hero& hero) : hero(hero)
{

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
				std::cout << "O";
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

void Labirintus::initHeroPosition(const unsigned int x, const unsigned int y)
{
	elems[y * LABIRINTUS_SIZE_X + x].setFoglalt();
	hero.setCurrentPadloelem(&elems[y * LABIRINTUS_SIZE_X + x]);
}