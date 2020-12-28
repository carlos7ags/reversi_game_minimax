from tiles import Tiles
from ai import Ai

MAX_DEPTH = 4


class Maze:
    """Draws the maze and handles interaction between Pacman and dots"""
    def __init__(self, WIDTH, HEIGHT, LENGTH, SQUARES, game_controller):
        self.LENGTH = LENGTH
        self.SQUARES = SQUARES
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.gc = game_controller
        self.tiles = Tiles(WIDTH, HEIGHT, LENGTH, SQUARES)

    def update(self):
        """Calculate score and check if a player wins every turn"""
        self.gc.player_score, self.gc.computer_score = self.tiles.det_winner()
        if self.tiles.winner == 1:
            self.gc.player_wins = True
        elif self.tiles.winner == 2:
            self.gc.computer_wins = True
        elif self.tiles.winner == "tie":
            self.gc.tie = True
        if self.tiles.gameover:
            self.gc.gameover = True

    def display(self):
        """Display the maze"""
        # Draw the maze walls
        stroke(0.0, 0.0, 0.0)
        strokeWeight(3)
        fill(0, 100, 0)
        rectMode(CORNER)

        x = -self.LENGTH
        for _ in range(self.SQUARES):
            x += self.LENGTH
            y = -self.LENGTH
            for _ in range(self.SQUARES):
                y += self.LENGTH
                rect(x, y, self.LENGTH, self.LENGTH)

        # Display the tiles
        self.tiles.display()
        self.update()

    def coords_to_square(self, x, y):
        """Transform pixel coordinates to spot coordinatesin maze"""
        x = x // self.LENGTH
        y = y // self.LENGTH
        return x, y

    def control(self, mouseX, mouseY):
        """Add a tile if player clicks in a valid spot"""
        x, y = self.coords_to_square(mouseX, mouseY)
        if (x, y) in self.tiles.valid_moves.keys():
            self.tiles.move(x, y)

    def auto(self):
        """Computer adds a tile optimizing with minimax"""
        x, y = Ai.minimax(self.tiles, MAX_DEPTH)
        self.tiles.move(x, y)
