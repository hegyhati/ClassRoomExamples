from typing import Optional, Tuple


class Position:
    def __init__(self, col: str = None, row: int = None,  text: str = None, ) -> None:
        if col != None and row != None:
            self.col = ord(col)-ord('a')
            self.row = row
        elif text != None:
            self.col = ord(text[0])-ord('a')
            self.row = int(text[1])
        else:
            raise ValueError

    def __str__(self) -> str:
        return chr(ord('a')+self.col) + str(self.row)

    def __eq__(self, other: 'Position') -> bool:
        return self.col == other.col and self.row == other.row

    def same_row(self, other: 'Position') -> bool:
        return self.row == other.row

    def same_column(self, other: 'Position') -> bool:
        return self.col == other.col

    def diagonal(self, other: 'Position') -> bool:
        return abs(self.row - other.row) == abs(self.col - other.col)

    def __sub__(self, other: 'Position') -> Tuple[int, int]:
        return (self.col - other.col, self.row-other.row)


class Piece:
    symbol = '?'

    def __init__(self, white: bool, position: Position) -> None:
        self.white = white
        self.position = position

    def is_friend(self, other: 'Piece') -> bool:
        return self.white == other.white

    def can_move_to(self, position: Position) -> bool:
        return False

    def get_symbol(self) -> str:
        return self.symbol

    def move(self, position: Position) -> None:
        self.position = position


class King(Piece):

    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♔' if white else '♚'

    def can_move_to(self, position: Position) -> bool:
        if self.position == position:
            return False
        elif self.position.col - position.col in [-1, 0, 1] and self.position.row - position.row in [-1, 0, 1]:
            return True
        else:
            return False


class Queen(Piece):
    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♕' if white else '♛'

    def can_move_to(self, position: Position) -> bool:
        return self.position.diagonal(position) or self.position.same_column(position) or self.position.same_row(position)


class Bishop(Piece):
    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♗' if white else '♝'

    def can_move_to(self, position: Position) -> bool:
        return self.position.diagonal(position)


class Knight(Piece):
    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♘' if white else '♞'

    def can_move_to(self, position: Position) -> bool:
        return (self.position - position) in {(1, -2), (1, 2), (-1, -2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1)}


class Rook(Piece):
    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♖' if white else '♜'

    def can_move_to(self, position: Position) -> bool:
        return self.position.same_column(position) or self.position.same_row(position)


class Pawn(Piece):

    def __init__(self, white: bool, position: Position) -> None:
        super().__init__(white, position)
        self.symbol = '♙' if white else '♟'

    def can_move_to(self, position: Position) -> bool:
        # todo: diagonal move
        # todo: double move
        if self.position.col != position.col:
            return False
        elif self.white and self.position.row == position.row - 1:
            return True
        elif not self.white and self.position.row == position.row + 1:
            return True
        else:
            return False


class ChessGame():
    columns = [chr(col+ord('a')) for col in range(8)]
    rows = list(range(1, 9))

    def __init__(self) -> None:
        self.pieces = [
            Rook(True, Position('a', 1)),
            Knight(True, Position('b', 1)),
            Bishop(True, Position('c', 1)),
            Queen(True, Position('d', 1)),
            King(True, Position('e', 1)),
            Bishop(True, Position('f', 1)),
            Knight(True, Position('g', 1)),
            Rook(True, Position('h', 1)),
            Pawn(True, Position('a', 2)),
            Pawn(True, Position('b', 2)),
            Pawn(True, Position('c', 2)),
            Pawn(True, Position('d', 2)),
            Pawn(True, Position('e', 2)),
            Pawn(True, Position('f', 2)),
            Pawn(True, Position('g', 2)),
            Pawn(True, Position('h', 2)),
            Rook(False, Position('a', 8)),
            Knight(False, Position('b', 8)),
            Bishop(False, Position('c', 8)),
            Queen(False, Position('d', 8)),
            King(False, Position('e', 8)),
            Bishop(False, Position('f', 8)),
            Knight(False, Position('g', 8)),
            Rook(False, Position('h', 8)),
            Pawn(False, Position('a', 7)),
            Pawn(False, Position('b', 7)),
            Pawn(False, Position('c', 7)),
            Pawn(False, Position('d', 7)),
            Pawn(False, Position('e', 7)),
            Pawn(False, Position('f', 7)),
            Pawn(False, Position('g', 7)),
            Pawn(False, Position('h', 7)),
        ]

    def get_piece_at(self, position: Position) -> Optional[Piece]:
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def print_board(self) -> None:
        for row in self.rows[::-1]:
            print(f" {row}: ", end='')
            for col in self.columns:
                piece = self.get_piece_at(Position(col, row))
                print(f" {'.' if piece == None else piece.get_symbol()} ", end='')
            print()
        print(f"    ", end='')
        for col in self.columns:
            print(f" {col} ", end='')
        print()

    def is_checkmate(self) -> bool:
        return False

    def is_stalemate(self) -> bool:
        return False

    def next_step(self):
        success = False
        while success == False:
            move = input('Next move (cr cr): ')
            p1, p2 = move.split(' ')  # todo: hibas bemenet
            from_position = Position(text=p1)
            to_position = Position(text=p2)
            piece = self.get_piece_at(from_position)
            if piece != None:
                if piece.can_move_to(to_position):
                    # not nice, todo check other pieces, etc.
                    piece.move(to_position)
                    success = True
                else:
                    print('Piece cannot move there.')
            else:
                print('No piece at that position.')


def main():
    game = ChessGame()
    while not game.is_checkmate() and not game.is_stalemate():
        game.print_board()
        game.next_step()


if __name__ == "__main__":
    main()
