#include "Player.h"

bool Player::hasWon()
{
	int i = 0;
	while (i < 4 && pieces[i].getRegion() == Piece::HOUSE)
		++i;
	return i == 4;
}

inline void Player::Piece::move(int length, int regionSize) {
	switch (region)
	{
	case Player::Piece::START:
		region = BOARD;
		index = 0;
		break;
	case Player::Piece::BOARD:
		index += length;
		if (index >= regionSize) {
			region = GARDEN;
			index -= regionSize;
		}
		break;
	case Player::Piece::GARDEN:
		index += length;
		if (index >= regionSize) {
			region = HOUSE;
			index -= regionSize;
		}
		break;
	default:
		break;
	}
}
