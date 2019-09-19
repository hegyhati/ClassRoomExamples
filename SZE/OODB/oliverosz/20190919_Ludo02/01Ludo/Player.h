#pragma once

#include "Ludo.h"

class Player {
public:
	class Piece;
	Player(int index, const Board* board) :
		pieces { Piece(board), Piece(board), Piece(board), Piece(board) },
		color('A' + index), board(board) {
		//color = 'A' + index;
	}
	bool hasWon() const;
	int decide(int rolled);
	char getColor() const { return color; }
	Piece& getPiece(int index) { return pieces[index]; }

	class Piece {
	public:
		Piece(const Board* board) : board(board) {
			region = START;
			index = 0;
		}
		enum Region { START, BOARD, GARDEN, HOUSE };
		Region getRegion() const { return region; }
		void setRegion(Region r) { region = r; }
		int getIndex() const { return index; }
		void move(int length, int regionSize);
	private:
		Region region;
		int index;
		const Board *board;
	};
private:
	Piece pieces[4];
	char color;
	const Board *board;
};
