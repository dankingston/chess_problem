import argparse
import math

from functools import cache

from board import ChessBoard, UnableToPlace
from pieces import Bishop, King, Knight, Piece, Queen, Rook
from stores import MemoryStore, RedisStore, Store


def get_parsed_args():
    parser = argparse.ArgumentParser(
        description="Chess Problem Solver",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--queens", type=int, help="Number of Queens", default=0)
    parser.add_argument("--kings", type=int, help="Number of Kings", default=0)
    parser.add_argument("--rooks", type=int, help="Number of Rooks", default=0)
    parser.add_argument("--bishops", type=int, help="Number of Bishops", default=0)
    parser.add_argument("--knights", type=int, help="Number of Knights", default=0)
    parser.add_argument("-M", type=int, help="Board width", default=4)
    parser.add_argument("-N", type=int, help="Board height", default=4)
    parser.add_argument("--store", type=str, help="Solution store (redis/memory)", default="memory")
    return parser.parse_args()


def get_pieces(parsed_args):
    # Order by most threatening i.e. queens remove the most possible available squares
    pieces = []
    pieces += [Queen()] * parsed_args.queens
    pieces += [Rook()] * parsed_args.rooks
    pieces += [Bishop()] * parsed_args.bishops
    pieces += [King()] * parsed_args.kings
    pieces += [Knight()] * parsed_args.knights
    return tuple(pieces)


@cache
def solve(chessboard, pieces: tuple[Piece], store: Store, restrict_piece: bool = False):
    piece = pieces[0]

    for x, y in chessboard.get_available_squares():
        # Try the first piece only in one quarter of the board - all other solutions are variants
        if restrict_piece and (
            y > math.ceil(chessboard.height / 2) or x > math.ceil(chessboard.width / 2)
        ):
            continue

        try:
            chessboard.place_piece(piece, x, y)
        except UnableToPlace:
            continue

        if len(pieces) == 1:
            store.add_solutions(chessboard.get_hash_key_variants())
        else:
            solve(chessboard, pieces[1:], store=store)

        chessboard.undo_last_piece(x, y)


if __name__ == "__main__":
    parsed_args = get_parsed_args()
    if parsed_args.store.lower() == "redis":
        store = RedisStore()
    else:
        store = MemoryStore()
    chessboard = ChessBoard(width=parsed_args.M, height=parsed_args.N)
    pieces = get_pieces(parsed_args)
    solve(chessboard, pieces, store=store, restrict_piece=True)
    print(f"Number of solutions: {store.get_solution_count()}")
