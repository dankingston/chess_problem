import pytest

from board import ChessBoard, UnableToPlace
from pieces import Bishop, King, Knight, Queen, Rook


def test_get_available_squares():
    board = ChessBoard(width=4, height=2)
    available_squares = set([s for s in board.get_available_squares()])
    assert available_squares == set([
        (0, 0), (1, 0), (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1), (3, 1),
    ])


def test_place_piece_and_undo():
    board = ChessBoard(width=4, height=3)
    assert board.hash_key == "............"
    board.place_piece(Rook(), 2, 1)
    assert board.hash_key == "......R....."
    board.place_piece(Knight(), 3, 0)
    assert board.hash_key == "...N..R....."
    board.place_piece(Rook(), 0, 2)
    assert board.hash_key == "...N..R.R..."
    assert board.available_squares == set([(1, 0)])
    assert board.piece_squares == set([(2, 1), (3, 0), (0, 2)])
    assert board.unavailable_squares_stack == [
        set([(2, 0), (0, 1), (1, 1), (3, 1), (2, 2)]),
        set(),
        set([(0, 0), (1, 2), (3, 2)]),
    ]
    board.undo_last_piece(0, 2)
    assert board.hash_key == "...N..R....."
    assert board.available_squares == set([(0, 0), (1, 0), (1, 2), (0, 2), (3, 2)])
    assert board.piece_squares == set([(2, 1), (3, 0)])
    assert board.unavailable_squares_stack == [
        set([(2, 0), (0, 1), (1, 1), (3, 1), (2, 2)]),
        set(),
    ]
    board.undo_last_piece(3, 0)
    assert board.hash_key == "......R....."
    board.undo_last_piece(2, 1)
    assert board.hash_key == "............"


def test_place_piece_fail():
    board = ChessBoard(width=3, height=3)
    board.place_piece(Rook(), 0, 0)
    with pytest.raises(UnableToPlace):
        board.place_piece(King(), 1, 1)


def test_get_hash_key_variants():
    board = ChessBoard(width=4, height=5)
    board.place_piece(Queen(), 1, 1)
    board.place_piece(Bishop(), 3, 0)
    board.place_piece(Knight(), 2, 4)
    assert board.hash_key == "...B.Q............N."
    assert set(board.get_hash_key_variants()) == set([
        "...B.Q............N.",  # original
        ".N............Q.B...",  # 180 rotation
        "B.....Q..........N..",  # x reflection
        "..N..........Q.....B",  # y reflection
    ])
