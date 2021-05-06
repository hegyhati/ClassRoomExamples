import random


class MemoryGame:

    def __init__(self, width=4, height=5):
        if width*height % 2 == 1:
            width += 1
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        tmp = list(range(self.width*self.height//2))
        tmp.extend(tmp)
        random.shuffle(tmp)
        self.board = []
        for h in range(self.height):
            self.board.append(tmp[h*self.width:(h+1)*self.width])
        self.revealed = [[False]*self.width for h in range(self.height)]

    def __check_coordinate(self, x: int, y: int) -> None:
        if x < 0 or x > self.width:
            raise Exception("Wrong x coordinate")
        if y < 0 or y > self.height:
            raise Exception("Wrong y coordinate")

    def get(self, x: int, y: int) -> int:
        self.__check_coordinate(x, y)
        return self.board[y][x]

    def try_pair(self, x1: int, y1: int, x2: int, y2: int) -> bool:
        value1 = self.get(x1, y1)
        value2 = self.get(x2, y2)
        if self.revealed[y1][x1] or self.revealed[y2][x2]:
            raise Exception("Already turned up cards")
        if value1 != value2:
            return False
        else:
            self.revealed[y1][x1] = self.revealed[y2][x2] = True
            return True

    def is_upward(self, x: int, y: int) -> bool:
        self.__check_coordinate(x, y)
        return self.revealed[y][x]

    def is_won(self) -> bool:
        for revealed_row in self.revealed:
            if False in revealed_row:
                return False
        return True


if __name__ == "__main__":
    m = MemoryGame()
    print(m.board)
    print(m.revealed)
