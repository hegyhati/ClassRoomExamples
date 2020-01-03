// LinkedList.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

#define _CRTDBG_MAP_ALLOC
#include <stdlib.h>
#include <crtdbg.h>

#include "LinkedList.h"

void linkedlisttest()
{
	Robot robot;
	robot.addPositionMeasurement(10, 10, 10);
	robot.addPositionMeasurement(10, 10, 15);
	robot.addPositionMeasurement(10, 7, 6);
	robot.stationaryMeasurment();
	robot.print();
}

int main()
{
	linkedlisttest();
	_CrtDumpMemoryLeaks();
}
