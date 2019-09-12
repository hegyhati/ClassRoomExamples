#include "Ludo.h"

Ludo::Ludo(int size, int gLength) {
	currentPlayer = 0;
	boardSize = size;
	gardenLength = gLength;
	for (int i = 0; i < 4; i++)
		players[i] = Player(i);
}

void Ludo::play()
{

}
