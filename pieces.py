from abc import ABC
from functools import cache


class Piece(ABC):
    letter = ""

    @cache
    def is_valid_move(self, move, max_x, max_y):
        move_x, move_y = move
        return (
            move_x <= max_x
            and move_x >= 0
            and move_y <= max_y
            and move_y >= 0
        )


class King(Piece):
    letter = "K"
    offsets = (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    )

    @cache
    def get_moves(self, x: int, y: int, max_x: int, max_y: int) -> set:
        """
        Gets all valid king moves from the current position
        """
        return set([
            (x + offset_x, y + offset_y)
            for offset_x, offset_y in self.offsets
            if self.is_valid_move((x + offset_x, y + offset_y), max_x, max_y)
        ])


class Queen(Piece):
    letter = "Q"
    offsets = (
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    )

    @cache
    def get_moves(self, x: int, y: int, max_x: int, max_y: int) -> set:
        """
        Gets all valid queen moves from the current position
        """
        limit = max(max_x, max_y)
        moves = []
        for offset_x, offset_y in self.offsets:
            for i in range(1, limit+1):
                move = (x + offset_x*i, y + offset_y*i)
                if self.is_valid_move(move, max_x, max_y):
                    moves.append(move)
                else:
                    break

        return set(moves)


class Rook(Piece):
    letter = "R"

    @cache
    def get_moves(self, x: int, y: int, max_x: int, max_y: int) -> set:
        """
        Gets all valid rook moves from the current position
        """
        moves = []
        for i in range(0, max_x+1):
            if i != x:
                moves.append((i, y))

        for j in range(0, max_y+1):
            if j != y:
                moves.append((x, j))

        return set(moves)


class Bishop(Piece):
    letter = "B"
    offsets = (
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    )

    @cache
    def get_moves(self, x: int, y: int, max_x: int, max_y: int) -> set:
        """
        Gets all valid bishop moves from the current position
        """
        limit = max(max_x, max_y)
        moves = []
        for offset_x, offset_y in self.offsets:
            for i in range(1, limit+1):
                move = (x + offset_x*i, y + offset_y*i)
                if self.is_valid_move(move, max_x, max_y):
                    moves.append(move)
                else:
                    break

        return set(moves)


class Knight(Piece):
    letter = "N"
    offsets = (
        (-2, 1),
        (-1, 2),
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
    )

    @cache
    def get_moves(self, x: int, y: int, max_x: int, max_y: int) -> set:
        """
        Gets all valid knight moves from the current position
        """
        return set([
            (x + offset_x, y + offset_y)
            for offset_x, offset_y in self.offsets
            if self.is_valid_move((x + offset_x, y + offset_y), max_x, max_y)
        ])
