from copy import deepcopy
from random import shuffle
from tiles import Tiles

WIDTH = 600
SQUARES = 4

def test_result():
    test = [(0, 1, 2, [[None, 1, None, None], [None, 1, 1, None],
             [None, 1, 2, None], [None, None, None, None]]),
            (2, 0, 1, [[None, 1, None, None], [None, 1, 1, None],
             [2, 2, 2, None], [None, None, None, None]])]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    for x, y, player, result in test:
        board.move(x, y)
        current_game = board.tiles_players
        assert result == current_game
        assert player == board.player