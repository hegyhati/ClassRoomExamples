#pragma once

#include <iostream>

class Position
{
private:
	double x;
	double y;
	double z;
public:
	Position(double x, double y, double z): x(x), y(y), z(z)
	{}
	Position(const Position& other)
	{
		x = other.x;
		y = other.y;
		z = other.z;
	}

	friend std::ostream& operator<<(std::ostream& os, const Position& pos);
};

std::ostream& operator<<(std::ostream& os, const Position& pos)
{
	os << '(' << pos.x << ',' << pos.y << ',' << pos.z << ')';
	return os;
}

struct LinkedListElement
{
	Position element;
	LinkedListElement* prev_element;
	LinkedListElement* next_element;	
};

class LinkedList
{
private:
	LinkedListElement* first_elem;
	LinkedListElement* last_elem;
public:
	LinkedList(): first_elem(NULL), last_elem(NULL)
	{}

	~LinkedList()
	{
		LinkedListElement* current_element = first_elem;
		while (current_element != NULL)
		{
			LinkedListElement* tmp = current_element;
			current_element = current_element->next_element;
			delete tmp;
		} 
	}

	void addElement(Position& position)
	{
		if (first_elem == NULL)
		{
			first_elem = new LinkedListElement({ position, NULL, NULL });
			last_elem = first_elem;
		}
		else
		{
			last_elem->next_element = new LinkedListElement({ position, last_elem, NULL });
			last_elem = last_elem->next_element;
		}
	}

	Position& last()
	{
		return last_elem->element;
	}

	Position& first()
	{
		return first_elem->element;
	}
};

LinkedList& operator+(LinkedList& list, Position& elem)
{
	list.addElement(elem);
	return list;
}

class Robot
{
private:
	LinkedList* measurements;
public:
	Robot()
	{
		measurements = new LinkedList();
	}

	~Robot()
	{
		delete measurements;
	}

	void addPositionMeasurement(double x, double y, double z)
	{
		Position p(x, y, z);
		measurements->addElement(p);
	}

	void stationaryMeasurment()
	{
		Position p0(measurements->last());
		measurements->addElement(p0);
	}
};

