from tile import Tile

global DIRECTIONS
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
              (0, 1), (1, -1), (1, 0), (1, 1)]


class Tiles:
    """A collection of tiles"""
    def __init__(self, WIDTH, HEIGHT, LENGTH, SQUARES):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.LENGTH = LENGTH
        self.SQUARES = SQUARES
        self.player = 1
        self.tiles = [[None for _ in range(SQUARES)] for _ in range(SQUARES)]
        self.valid_moves = {}
        self.gameover = False
        self.winner = None
        self.initial_state()

    def initial_state(self):
        """Create four initial tiles in center and get valid moves"""
        first_pos = (self.SQUARES//2)
        second_pos = (self.SQUARES//2) - 1
        self.add_tile(second_pos, first_pos, player=1)
        self.add_tile(first_pos, first_pos, player=2)
        self.add_tile(first_pos, second_pos, player=1)
        self.add_tile(second_pos, second_pos, player=2)
        self.get_valid_moves()

    def move(self, x, y):
        """Add computer/player move and update game status"""
        self.add_tile(x, y)
        self.color_tiles(x, y)
        self.spaces_over()
        self.next_player()
        self.get_valid_moves()
        self.check_next_moves()

    def add_tile(self, x, y, player=None):
        """Create a tile in board"""
        player = player if player else self.player
        self.tiles[x][y] = Tile(x, y, self.LENGTH, player)

    def color_tiles(self, x, y):
        """Update color for tiles after move"""
        for i, j in self.valid_moves[(x, y)]:
            self.tiles[i][j].player = self.player

    def get_valid_moves(self):
        """Get a dictionary of current valid moves and tiles to flip"""
        self.valid_moves = {}
        for i in range(self.SQUARES):
            for j in range(self.SQUARES):
                tiles_fliped = self.tiles_fliped(i, j)
                if tiles_fliped:
                    self.valid_moves[(i, j)] = tiles_fliped

    def tiles_fliped(self, x, y):
        """Check if valid move with flipped tiles"""
        # Check if tile already in place
        if self.tiles[x][y]:
            return False
        # Evaluate if one location changes colors
        tiles_fliped = []
        for loc in DIRECTIONS:
            tiles_fliped += self.tiles_fliped_direction(x, y, loc)
        return tiles_fliped

    def tiles_fliped_direction(self, x, y, loc):
        """Check for tiles to flip in every valid direction"""
        tiles_fliped = []
        x, y = x + loc[0], y + loc[1]
        if not self.in_array(x, y) or not self.tiles[x][y]:
            return []
        if self.tiles[x][y].player == self.player:
            return []
        tiles_fliped.append((x, y))
        while True:
            x, y = x + loc[0], y + loc[1]
            if not self.in_array(x, y) or not self.tiles[x][y]:
                break
            if self.tiles[x][y].player == self.player:
                return tiles_fliped
            tiles_fliped.append((x, y))
        return []

    def next_player(self):
        """Updates current player every turn"""
        if self.player == 2:
            self.player = 1
        else:
            self.player = 2

    def spaces_over(self):
        """Check if all spots al filled with a tile"""
        if sum([row.count(None) for row in self.tiles]) == 0:
            self.gameover = True

    @property
    def valid_moves_over(self):
        """Check if valid moves in maze"""
        if len(self.valid_moves.keys()) < 1:
            return True

    def check_next_moves(self):
        """Check if valid moves in next two turns"""
        if self.valid_moves_over:
            self.next_player()
            self.get_valid_moves()
        if self.valid_moves_over:
            self.gameover = True

    def in_array(self, x, y):
        """Check if coordinates are in maze"""
        if x >= 0 and y >= 0 and x < self.SQUARES and y < self.SQUARES:
            return True
        return False

    def det_winner(self):
        """Check if winner"""
        if self.gameover:
            player_score, computer_score = self.score
            if player_score > computer_score:
                self.winner = 1
            elif player_score < computer_score:
                self.winner = 2
            else:
                self.winner = "tie"
            return (player_score, computer_score)
        return (None, None)

    @property
    def utility(self):
        """Returns 1 if computer won, -1 if player won, 0 otherwise."""
        if self.winner == 2:
            return -1
        elif self.winner == 1:
            return 1
        elif self.winner == "tie":
            return 0
        else:
            None

    @property
    def score(self):
        """Calculates score counting tiles by color"""
        player = 0
        computer = 0
        current_tiles = [tile for row in self.tiles for tile in row]
        for tile in current_tiles:
            if isinstance(tile, Tile):
                if tile.player == 1:
                    player += 1
                elif tile.player == 2:
                    computer += 1
        return player, computer

    @property
    def tiles_players(self):
        return [[tile.player if tile else None for tile in subrow]
                for subrow in self.tiles]

    @staticmethod
    def players_tiles(tiles):
        return [[Tile(1, 1, 1, player) if player
                 else None for player in subrow]
                for subrow in tiles]

    def display(self):
        """Calls each tile's display method"""
        [[tile.display() if tile else None for tile in row]
         for row in self.tiles]

        fill(255, 0, 0)
        textSize(15)
        textAlign(LEFT, TOP)
        current_player = "Next player: %s" % self.player
        text(current_player, 10, 10)
