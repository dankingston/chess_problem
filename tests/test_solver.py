from board import ChessBoard
from pieces import King, Knight, Rook
from stores import MemoryStore
from solver import solve


def test_solver_3x3():
    chessboard = ChessBoard(width=3, height=3)
    pieces = (Rook(), King(), King())
    store = MemoryStore()
    solve(chessboard, pieces, store=store, restrict_piece=True)
    assert store.get_solution_count() == 4
    assert store.get_solutions() == set([
        ".R....K.K",
        "..KR....K",
        "K.K....R.",
        "K....RK..",
    ])


def test_solver_4x4():
    chessboard = ChessBoard(width=4, height=4)
    pieces = (Rook(), Rook(), Knight(), Knight(), Knight(), Knight())
    store = MemoryStore()
    solve(chessboard, pieces, store=store, restrict_piece=True)
    assert store.get_solution_count() == 8
