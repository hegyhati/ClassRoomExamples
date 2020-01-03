// ForestExample.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

class Creature
{
protected:
	double mass;
	const double energy;
	bool alive;
public:
	Creature(double mass, double energy) : 
		mass(mass), 
		energy(energy), 
		alive(true) {}

	virtual double nutrition()
	{
		return mass*energy;
	}

	virtual void harvest() = 0;

	bool isAlive()
	{
		return alive;
	}

	void kill()
	{
		alive = false;
	}
};

class Plant: public Creature
{
private:
	const double collagen_ratio;
	const double growth_ratio;
public:
	Plant(const double collagen_ratio, double mass, double energy) : Creature(mass, energy), collagen_ratio(collagen_ratio), growth_ratio(0.04) {}

	virtual double nutrition()
	{
		return collagen_ratio * mass * energy;
	}

	void grow()
	{
		if (mass > 0.0)
		{
			mass += growth_ratio * mass;
		}
		else
		{
			mass = 0.1;
		}
	}

	virtual void harvest()
	{
		mass = 0;
	}
};

class Animal: public Creature
{
private:
	const double metabolism_rate;
public:
	Animal(const double metabolism_rate, double mass, double energy) : Creature(mass, energy), metabolism_rate(metabolism_rate) {}

	virtual void eat(Creature* creature) = 0;
	virtual void metabolism()
	{
		if (mass > 0.0)
		{
			mass -= metabolism_rate * mass;
		}
		else
		{
			mass = 0.0;
			kill();
		}
	}
};

class Rabbit: public Animal
{
public:
	Rabbit(double metabolism_rate, double mass, double energy) : Animal(0.01, mass, energy) {}

	virtual void eat(Creature* creature)
	{
		if (dynamic_cast<Plant*>(creature) 
			!= nullptr && creature->isAlive())
		{
			std::cout << "Rabbit eats the plant" << std::endl;
			mass += creature->nutrition();
			creature->harvest();
		}
	}

	virtual void harvest()
	{
		kill();
		mass = 0;
	}
};

class Fox : public Animal
{
public:
	Fox(double metabolism_rate, double mass, double energy) : Animal(0.05, mass, energy) {}

	virtual void eat(Creature* creature)
	{
		if (dynamic_cast<Rabbit*>(creature) != nullptr 
			&& creature->isAlive())
		{
			std::cout << "Fox eats the rabbit" << std::endl;
			mass += creature->nutrition();
			creature->harvest();
		}
	}

	virtual void harvest()
	{
		kill();
		mass = 0;
	}

};

class Forest
{
private:
	Creature** creatures;
	unsigned int current_creatures;
	unsigned int max_creatures;
public:
	Forest(int max_creatures) : current_creatures(0), max_creatures(max_creatures), creatures(new Creature* [max_creatures]) {}

	void addCreature(Creature* creature)
	{
		if (current_creatures < max_creatures)
		{
			creatures[current_creatures] = creature;
			current_creatures++;
		}
	}

	~Forest()
	{
		for (unsigned int i = 0; i < current_creatures; i++)
		{
			delete creatures[i];
		}
		delete[] creatures;
	}

	void printForest()
	{
		for (unsigned int i = 0; i < current_creatures; i++)
		{
			if (dynamic_cast<Plant*>(creatures[i])
				!=nullptr)
			{
				std::cout << "There is a plant\n";
			}
			else if (dynamic_cast<Rabbit*>(creatures[i]) 
				!= nullptr)
			{
				std::cout << "There is a rabbit\n";
			}
			else if (dynamic_cast<Fox*>(creatures[i]) 
				!= nullptr)
			{
				std::cout << "There is a fox\n";
			}
		}
	}

	void simulate()
	{
		for (unsigned int i = 0; i < current_creatures; i++)
		{
			Animal* animal = dynamic_cast<Animal*>(creatures[i]);
			if (animal != nullptr)
			{
				for (unsigned int j = 0; j < current_creatures; j++)
				{
					animal->eat(creatures[j]);
				}
				
			}
		}
	}
};



void forestProgram()
{
	Forest* forest = new Forest(40);
	forest->addCreature(new Plant(0.4, 1, 100));
	forest->addCreature(new Plant(0.4, 1, 100));
	forest->addCreature(new Plant(0.4, 1, 100));
	forest->addCreature(new Rabbit(0.4, 1, 100));
	forest->addCreature(new Rabbit(0.4, 1, 100));
	forest->addCreature(new Fox(0.4, 1, 100));
	forest->printForest();
	forest->simulate();
	delete forest;
}

int main(int argc, char** argv)
{
	forestProgram();
	_CrtDumpMemoryLeaks();
	return 0;
}
