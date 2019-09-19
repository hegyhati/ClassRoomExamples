#pragma once

class Player {
public:
	Player(int index=0) {
		color = 'A' + index;
	}
	bool hasWon();
	int decide(int rolled);

	class Piece {
	public:
		Piece() {
			region = START;
			index = 0;
		}
		enum Region { START, BOARD, GARDEN, HOUSE };
		Region getRegion() { return region; }
		void setRegion(Region r) { region = r; }
		int getIndex() { return index; }
		void move(int length, int regionSize);
	private:
		Region region;
		int index;
	};
private:
	Piece pieces[4];
	char color;
};