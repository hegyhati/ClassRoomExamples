#pragma once

#include "Board.h"
#include "Player.h"

class Ludo {
public:
	Ludo(int size = 48, int gardenLength = 6);
	void play();
private:
	Player players[4];
	int currentPlayer;
	const Board board;

	void display();
	bool turn();
	int roll();
	// distance between player start fields
	int offset() { return board.boardSize / 4; }
};