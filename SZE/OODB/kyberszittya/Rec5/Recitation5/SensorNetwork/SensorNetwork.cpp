// SensorNetwork.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <list>
#include <map>
#include <string>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

class Sensor
{
private:
	std::list<double> values;
	const std::string name;
public:
	Sensor(const std::string name) : name(name) {}

	virtual void measure() = 0;

	void printValues()
	{
		for (const auto& v : values)
		{
			std::cout << v << '\n';
		}
	}

	std::string getName() const
	{
		return name;
	}
};

class TemperatureSensor: public Sensor
{
private:
	double temperature;
	
public:
	TemperatureSensor(const std::string name): Sensor(name){}

	double getTemperature()
	{
		return temperature;
	}

	virtual void measure()
	{
		temperature = 0.0;
	}
};

class PressureSensor : public Sensor
{
private:
	double pressure;
public:
	PressureSensor(const std::string name) : Sensor(name) {}

	virtual void measure()
	{
		pressure = 0.0;
	}

	double getPressure()
	{
		return pressure;
	}
};

class Network
{
private:
	std::string name;
	std::map<std::string, Sensor*> sensors;
public:
	Network(std::string name): name(name){}

	void addSensor(Sensor* sensor)
	{
		sensors[sensor->getName()] = sensor;
	}

	~Network()
	{
		for (const auto& a : sensors)
		{
			delete a.second;
		}
	}

	void printCurrentValues()
	{
		for (const auto& a : sensors)
		{
			std::cout << a.first << '\t';
			if (dynamic_cast<TemperatureSensor*>(a.second) != nullptr) 
			{
				std::cout << dynamic_cast<TemperatureSensor*>(a.second)->getTemperature();
			}
			else if (dynamic_cast<PressureSensor*>(a.second) != nullptr)
			{
				std::cout << dynamic_cast<PressureSensor*>(a.second)->getPressure();
			}
			std::cout << '\n';
		}
	}
};


void clsuterExample()
{
	Network network("Home");
	network.addSensor(new TemperatureSensor("BMP110"));
	network.addSensor(new PressureSensor("PRES22"));
	network.addSensor(new TemperatureSensor("BMP111_2"));
	network.printCurrentValues();
}

int main(int argc, char**argv)
{
	clsuterExample();
	_CrtDumpMemoryLeaks();
	return 0;
}