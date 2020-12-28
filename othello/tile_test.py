from tile import Tile


def test__init__():
    """Test init method for a tile"""
    arguments = [(100, 105, 10, 1), (1, 8, 5, 2), (950, 1050, 0, 1)]
    for args in arguments:
        tile = Tile(*args)
        assert (tile.x, tile.y, tile.dimension, tile.player) == args