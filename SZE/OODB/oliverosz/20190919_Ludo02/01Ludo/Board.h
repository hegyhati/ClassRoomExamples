#pragma once

struct Board {
	int boardSize;
	int gardenLength;
	Board(int size, int gLength) : boardSize(size), gardenLength(gLength)
	{
	}
};