#include "Ludo.h"

#include <cstdlib>
#include <ctime>

#include <iostream>
using namespace std;

Ludo::Ludo(int size, int gLength) :
	board(size, gLength),
	players{ Player{0, &board}, Player{1, &board}, Player{2, &board}, Player{3, &board} }
{
	currentPlayer = 0;
	//for (int i = 0; i < 4; i++)
	//	players[i] = Player(i);
	srand(time(nullptr));
}

void Ludo::play()
{
	bool won;
	do {
		won = turn();
		if (won) {
			cout << "Player " << players[currentPlayer].getColor() << " has won!\n";
		}
		currentPlayer++;
		if (currentPlayer >= 4) currentPlayer = 0;
	} while (!won);
}

bool Ludo::turn()
{
	int rolled = roll();
	int chosenPiece = players[currentPlayer].decide(rolled);
	Player::Piece& piece = players[currentPlayer].getPiece(chosenPiece);
	piece.move(rolled, piece.getRegion() == Player::Piece::BOARD ? board.boardSize : board.gardenLength);
	// check if another player piece is there
	// if there is one, send it back to start
	for (int opponent = 0; opponent < 4; ++opponent) {
		if (opponent == currentPlayer) continue;
		for (int i = 0; i < 4; ++i) {
			Player::Piece& other = players[opponent].getPiece(i);
			if (piece.getRegion() == Player::Piece::BOARD && other.getRegion() == Player::Piece::BOARD)
			{
				// translate indices to the same coordinate system
				int piecePos = piece.getIndex() + currentPlayer * offset();
				piecePos = piecePos % board.boardSize;
				int otherPos = other.getIndex() + opponent * offset();
				otherPos = otherPos % board.boardSize;
				if (piecePos == otherPos)
					other.setRegion(Player::Piece::START);
			}
		}
	}
	return players[currentPlayer].hasWon();
}

int Ludo::roll()
{
	return rand() % 6 + 1;
}
