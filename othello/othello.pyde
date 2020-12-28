from maze import Maze
from game_controller import GameController

WIDTH = 600
HEIGHT = 600
SQUARES = 8
LENGTH = WIDTH // SQUARES

global timer
timer = 0
WAIT_TIME = 1000

game_controller = GameController(WIDTH, HEIGHT)
maze = Maze(WIDTH, HEIGHT, LENGTH, SQUARES, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


def draw():
    background(0)
    maze.display()
    computer_move()
    ask_player_score()
    game_controller.update()


def mousePressed():
    """User move when click in x, y coordinates"""
    global timer
    if maze.tiles.player == 1 and not maze.tiles.gameover:
        timer = millis()
        maze.control(mouseX, mouseY)


def computer_move():
    """Computer move after user click"""
    global timer
    if (millis() > timer + WAIT_TIME and
            maze.tiles.player == 2 and not maze.tiles.gameover):
        maze.auto()


def user_input(message=''):
    """Prompt name to user"""
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def write_user_score(name, score):
    """Writes player's score to text file"""
    filename = "scores.txt"
    try:
        with open(filename, "r") as f:
            first_line = f.readline()
    except IOError:
        first_line = ""
    if first_line:
        top_name, top_score = tuple(first_line.split())
        if int(top_score) > score:
            with open(filename, "a") as f:
                f.write("%s %d\n" % (name, score))
        else:
            with open(filename, "r+") as f:
                content = f.read()
                f.seek(0, 0)
                text = "%s %d\n" % (name, score)
                f.write(text + content)
    else:
        with open(filename, "a+") as f:
            f.write("%s %d\n" % (name, score))


def ask_player_score():
    """Prompts player's name to write score in file"""
    global timer
    if millis() > timer + WAIT_TIME and game_controller.ask_user:
        player_name = user_input("Enter your name: ")
        player_name = player_name if player_name else "None"
        write_user_score(player_name, game_controller.player_score)
        noLoop()

global count
count = 0
def foo(m, n):
    global count
    count += 1
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return foo(m-1, 1)
    elif m > 0 and n > 0:
        return foo(m-1, foo(m, n-1))
foo(1, 0)


def bubble_sort(array):

    for _ in range(len(array)):
        swapped = True
        for j in range(1,len(array)):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                swapped = False
        print(_, ": ", array)

        # If we went through the whole array and never swapped anything
        # then the array must be sorted and we can exit early
        if swapped:
            return

bubble_sort([5,7,3,4,5,6,0])