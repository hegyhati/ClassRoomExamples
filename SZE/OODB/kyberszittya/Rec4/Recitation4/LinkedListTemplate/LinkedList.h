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

template<class T> struct LinkedListElement
{
	T element;
	LinkedListElement<T>* prev_element;
	LinkedListElement<T>* next_element;	
};

template<class T> class LinkedList
{
private:
	LinkedListElement<T>* first_elem;
	LinkedListElement<T>* last_elem;
public:
	LinkedList(): first_elem(NULL), last_elem(NULL)
	{}

	~LinkedList()
	{
		LinkedListElement<T>* current_element = first_elem;
		while (current_element != NULL)
		{
			LinkedListElement<T>* tmp = current_element;
			current_element = current_element->next_element;
			delete tmp;
		} 
	}

	

	T& last()
	{
		return last_elem->element;
	}

	T& first()
	{
		return first_elem->element;
	}

	void print()
	{
		LinkedListElement<T>* current_element = first_elem;
		while (current_element != NULL)
		{
			std::cout << current_element->element << std::endl;
			current_element = current_element->next_element;
		}
	}
	
	void addElement(T& position)
	{
		if (first_elem == NULL)
		{
			first_elem = new LinkedListElement<T>({ position, NULL, NULL });
			last_elem = first_elem;
		}
		else
		{
			last_elem->next_element = new LinkedListElement<T>({ position, last_elem, NULL });
			last_elem = last_elem->next_element;
		}
	}
};


template <class T> LinkedList<T>& operator+(LinkedList<T>& list, Position& elem)
{
	list.addElement(elem);
	return list;
}

class Robot
{
private:
	LinkedList<Position>* measurements;
public:
	Robot()
	{
		measurements = new LinkedList<Position>();
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

	void print()
	{
		measurements->print();
	}
};

