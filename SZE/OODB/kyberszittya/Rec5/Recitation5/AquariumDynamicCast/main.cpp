// AquariumDynamicCast.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

class Fish
{
private:
	double mass;
public:
	Fish(double mass): mass(mass){}

	virtual void speak()
	{
		std::cout << "I am a fish" << std::endl;
	}

	virtual void swim()
	{
		std::cout << "Fish swimming" << std::endl;
	}
};

class Trout: public Fish
{
public:
	Trout() : Fish(10) {};

	virtual void speak()
	{
		std::cout << "I am a trout" << std::endl;
	}
};

class Carp : public Fish
{
public:
	Carp() : Fish(20) {};

	void floating()
	{
		std::cout << "Carp floats\n";
	}

	virtual void speak()
	{
		floating();
		std::cout << "I am a carp" << std::endl;
	}
};

class Shark: public Fish
{
public:
	Shark() : Fish(1000) {}

	virtual void speak()
	{
		std::cout << "I am a shark" << std::endl;
	}
};

class Aquarium
{
private:
	Fish** fishes;
	unsigned int current_fishes;
	const unsigned int max_fishes;
public:
	Aquarium(const unsigned int max_fishes): 
		current_fishes(0), 
		max_fishes(max_fishes), 
		fishes(new Fish*[max_fishes]) {}

	~Aquarium()
	{
		for (unsigned int i = 0; i < current_fishes; i++)
		{
			delete fishes[i];
		}
		delete[] fishes;
	}

	void insertFish(Fish* fish)
	{
		if (current_fishes < max_fishes)
		{
			fishes[current_fishes] = fish;
			current_fishes++;
		}
		else
		{
			std::cerr << "Aquarium is full";
		}
	}

	void speakAllFish()
	{
		for (unsigned int i = 0; i < current_fishes; i++)
		{
			fishes[i]->speak();
		}
	}

	void feedFish()
	{
		for (unsigned int i = 0; i < current_fishes; i++)
		{

		}
	}
};

void aquariumExample()
{
	Aquarium aquarium(10);
	aquarium.addFish(new Trout());
	aquarium.addFish(new Trout());
	aquarium.addFish(new Fish(1.0));
	aquarium.addFish(new Shark());
	aquarium.addFish(new Carp());
	aquarium.speakAllFish();
}

int main(int argc, char ** argv)
{
	aquariumExample();
	_CrtDumpMemoryLeaks();
	return 0;
}
