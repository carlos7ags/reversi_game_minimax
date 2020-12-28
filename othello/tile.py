
class Tile:
    """A tile"""
    def __init__(self, x, y, dimension, player):
        self.x_coord = (x*dimension) + (dimension/2)
        self.y_coord = (y*dimension) + (dimension/2)
        self.x = x
        self.y = y
        self.dimension = dimension
        self.player = player
        self.TILE_DIM = dimension*0.8

    def display(self):
        """Draws the tile"""
        if self.player == 1:
            fill(0.0, 0.0, 0.0)
        else:
            fill(1.0, 1.0, 1.0)
        noStroke()
        ellipse(self.x_coord, self.y_coord, self.TILE_DIM, self.TILE_DIM)
