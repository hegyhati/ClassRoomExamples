#pragma once

#include "Player.h"

class Ludo {
public:
	Ludo(int size = 48, int gardenLength = 6);
	void play();
private:
	Player players[4];
	int currentPlayer;
	int boardSize;
	int gardenLength;

	void display();
	bool turn();
	int roll();
};