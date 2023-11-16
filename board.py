from textwrap import wrap

from pieces import Piece


class UnableToPlace(Exception):
    pass


class ChessBoard:
    blank_character = "."

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.available_squares = set(
            [(x, y) for x in range(width) for y in range(height)]
        )
        self.hash_key = self.blank_character * width * height
        self.piece_squares = set([])
        self.unavailable_squares_stack = []

    def place_piece(self, piece: Piece, x: int, y: int):
        moves = piece.get_moves(x, y, self.width-1, self.height-1)
        if moves.intersection(self.piece_squares):
            raise UnableToPlace

        self.available_squares.remove((x, y))

        # Add to stack of unavailable squares so that we can undo this piece placement
        self.unavailable_squares_stack.append(
            moves.intersection(self.available_squares)
        )
        self.available_squares.difference_update(moves)
        self.piece_squares.add((x, y))
        self.update_hash_key(x, y, piece.letter)

    def undo_last_piece(self, x: int, y: int):
        self.piece_squares.remove((x, y))
        self.available_squares.add((x, y))
        self.available_squares.update(self.unavailable_squares_stack.pop())
        self.update_hash_key(x, y, self.blank_character)

    def update_hash_key(self, x: int, y: int, char: str):
        index = self.width * y + x
        self.hash_key = self.hash_key[:index] + char + self.hash_key[index+1:]

    def as_string(self, seperator: str = "\n"):
        return seperator.join(wrap(self.hash_key, self.width))

    def __str__(self) -> str:
        return self.as_string()

    def get_available_squares(self):
        iterated = set([])
        while True:
            try:
                item = next(iter(self.available_squares.difference(iterated)))
                iterated.add(item)
                yield item
            except StopIteration:
                return

    def get_hash_key_variants(self):
        rotation = self.hash_key[::-1]
        rows = wrap(self.hash_key, self.width)
        x_reflection = "".join([row[::-1] for row in rows])
        y_reflection = "".join(reversed(rows))
        return (self.hash_key, rotation, x_reflection, y_reflection)

    def __hash__(self):
        return hash(self.hash_key)
