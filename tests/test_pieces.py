from pieces import Bishop, King, Knight, Queen, Rook


def test_king():
    piece = King()
    moves = piece.get_moves(x=3, y=1, max_x=4, max_y=3)
    assert moves == set([(3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (2, 1), (2, 0)])

    moves = piece.get_moves(x=0, y=3, max_x=3, max_y=3)
    assert moves == set([(0, 2), (1, 2), (1, 3)])


def test_queen():
    piece = Queen()
    moves = piece.get_moves(x=1, y=1, max_x=3, max_y=4)
    assert moves == set([
        (0, 0), (2, 2), (3, 3), (2, 0), (0, 2),
        (1, 0), (2, 1), (3, 1), (1, 2), (1, 3), (1, 4), (0, 1),
    ])

    moves = piece.get_moves(x=3, y=1, max_x=3, max_y=3)
    assert moves == set([
        (2, 0), (3, 0),
        (0, 1), (1, 1), (2, 1),
        (2, 2), (3, 2),
        (1, 3), (3, 3),
    ])


def test_rook():
    piece = Rook()
    moves = piece.get_moves(x=0, y=0, max_x=3, max_y=3)
    assert moves == set([
        (0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0),
    ])


def test_bishop():
    piece = Bishop()
    moves = piece.get_moves(x=1, y=1, max_x=3, max_y=4)
    assert moves == set([(0, 0), (2, 2), (3, 3), (2, 0), (0, 2)])


def test_knight():
    piece = Knight()
    moves = piece.get_moves(x=0, y=1, max_x=3, max_y=3)
    assert moves == set([(2, 0), (2, 2), (1, 3)])

    moves = piece.get_moves(x=5, y=3, max_x=7, max_y=7)
    assert moves == set([(6, 1), (7, 2), (7, 4), (6, 5), (4, 5), (3, 4), (3, 2), (4, 1)])
