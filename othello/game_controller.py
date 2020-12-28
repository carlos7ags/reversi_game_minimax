
class GameController:
    """Maintains the state of the game."""
    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player_wins = False
        self.computer_wins = False
        self.tie = False
        self.player_score = None
        self.computer_score = None
        self.gameover = None
        self.ask_user = False

    def update(self):
        """Carries out necessary actions if computer or player wins"""
        if self.computer_wins:
            fill(255, 0, 0)
            textSize(30)
            textAlign(CENTER, CENTER)
            score_text = "Computer scored: %s" % self.computer_score
            text("GAME OVER! COMPUTER WINS\n" + score_text,
                 self.WIDTH/2, self.HEIGHT/2)
            self.ask_user = True
        if self.player_wins:
            fill(255, 0, 0)
            textSize(30)
            textAlign(CENTER, CENTER)
            score_text = "You scored %s" % self.player_score
            text("GAME OVER! YOU WIN!!!\n" + score_text,
                 self.WIDTH/2, self.HEIGHT/2)
            self.ask_user = True
        if self.tie:
            fill(255, 0, 0)
            textSize(30)
            textAlign(CENTER, CENTER)
            score_text = "Both scored %s" % self.player_score
            text("GAME OVER! NO ONE WINS\n" + score_text,
                 self.WIDTH/2, self.HEIGHT/2)
            self.ask_user = True
