from tile import Tile
from tiles import Tiles

global DIRECTIONS
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

WIDTH = 600
SQUARES = 4

def test__init__():
    test = [(2, [[2, 1], [1, 2]]),
            (4, [[None, None, None, None], [None, 2, 1, None],
                 [None, 1, 2, None], [None, None, None, None]])]
    for squares, tiles in test:
        board = Tiles(WIDTH, WIDTH, WIDTH//squares, squares)
        initial_game = board.tiles_players
        assert tiles == initial_game


def test_add_tile():
    test = [(1, 0, None, [[None, None, None, None], [1, 2, 1, None],
             [None, 1, 2, None], [None, None, None, None]]),
            (3, 3, 2, [[None, None, None, None], [1, 2, 1, None],
             [None, 1, 2, None], [None, None, None, 2]])]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    for x, y, player, result in test:
        board.add_tile(x, y, player)
        current_game = board.tiles_players
        assert result == current_game


def test_color_tiles():
    test = [(0, 1, [[None, None, None, None], [None, 1, 1, None],
                 [None, 1, 2, None], [None, None, None, None]]),
            (1, 0, [[None, None, None, None], [None, 1, 1, None],
             [None, 1, 2, None], [None, None, None, None]]),
            (2, 3, [[None, None, None, None], [None, 2, 1, None],
             [None, 1, 1, None], [None, None, None, None]]),
            (3, 2, [[None, None, None, None], [None, 2, 1, None],
             [None, 1, 1, None], [None, None, None, None]])
            ]
    for x, y, result in test:
        board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
        board.color_tiles(x, y)
        assert result == board.tiles_players


def test_get_valid_moves():
    test = [(0, 1, {(0, 0): [(1, 1)], (0, 2): [(1, 2)], (2, 0): [(2, 1)]}),
            (2, 0, {(3, 0): [(2, 1)], (3, 1): [(2, 1)], (3, 2): [(2, 2)], (3, 3): [(2, 2)]})]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    for x, y, result in test:
        board.move(x, y)
        assert result == board.valid_moves


def test_next_player():
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    assert board.player == 1
    board.next_player()
    assert board.player == 2
    board.next_player()
    assert board.player == 1

def test_spaces_over():
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    board.spaces_over()
    assert board.gameover == False
    new_tile = Tile(10, 10, 10, 1)
    board.tiles = [[new_tile for _ in subrow] for subrow in board.tiles]
    board.spaces_over()
    assert board.gameover == True


def test_valid_moves_over():
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    assert board.valid_moves_over == None
    new_tile = Tile(10, 10, 10, 1)
    board.tiles = [[new_tile for _ in subrow] for subrow in board.tiles]
    board.get_valid_moves()
    assert board.valid_moves_over == True


def test_score():
    test = [(7, 3, [[1, 1, None, 2], [1, 1, 1, None],
         [None, 1, 2, 2], [1, None, None, None]]),
        (4, 4, [[None, 2, None, 2], [None, 1, 1, None],
         [None, None, 2, 1], [1, 2, None, None]]),
        (7, 8, [[1, 2, 2, 1], [2, 2, 1, 2],
         [2, 1, 1, 1], [2, 1, 2, None]]),
        (11, 5, [[2, 1, 1, 1], [2, 2, 1, 2],
         [1, 1, 1, 1], [1, 1, 2, 1]])
        ]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    for player_score, computer_score, tiles in test:
        board.tiles = board.players_tiles(tiles)
        assert (player_score, computer_score) == board.score


def test_determine_winner():
    test = [(1, [[1, 1, None, 2], [1, 1, 1, None],
                    [None, 1, 2, 2], [1, None, None, None]]),
            ("tie", [[None, 2, None, 2], [None, 1, 1, None],
                    [None, None, 2, 1], [1, 2, None, None]]),
            (2, [[1, 2, 2, 1], [2, 2, 1, 2],
                    [2, 1, 1, 1], [2, 1, 2, None]]),
            (1, [[2, 1, 1, 1], [2, 2, 1, 2],
                     [1, 1, 1, 1], [1, 1, 2, 1]])
            ]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    board.gameover = True
    for winner, tiles in test:
        board.tiles = board.players_tiles(tiles)
        board.determine_winner()
        assert winner == board.winner


def test_utility():
    test = [(1, 1), ("tie", 0), (2, -1)]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    for winner, utility in test:
        board.winner = winner
        assert board.utility == utility


def test_tiles_players():
    test = [[None, None, None, None], [None, 2, 1, None],
                 [None, 1, 2, None], [None, None, None, None]]
    board = Tiles(WIDTH, WIDTH, WIDTH // SQUARES, SQUARES)
    tiles = board.tiles_players
    assert tiles == test





