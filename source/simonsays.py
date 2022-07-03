"""Simon Says
 
Exercises

1. Speed up tile flash rate.
2. Add more tiles.
"""

from random import choice
from time import sleep
import turtle

from utils import floor, square, vector

pattern = []
guesses = []
tiles = {
    vector(-100, -100): ('red', 'dark red'),
    vector(-100, -300): ('blue', 'dark blue'),
    vector(-300, -100): ('green', 'dark green'),
    vector(-300, -300): ('yellow', 'khaki'),
    vector(-100, 100): ('mediumorchid', 'purple'),
    vector(-300, 100): ('mediumturquoise', 'lightseagreen'),
    vector(100, -300): ('orange', 'wheat'),
    vector(100, -100): ('gray', 'darkgray'),
    vector(100, 100): ('deeppink', 'hotpink'),
}


def grid():
    """Draw grid of tiles."""
    square(-100, -100, 200, 'dark red')
    square(-100, -300, 200, 'dark blue')
    square(-300, -100, 200, 'dark green')
    square(-300, -300, 200, 'khaki')
    square(-100, 100, 200, 'purple')
    square(-300, 100, 200, 'lightseagreen')
    square(100, -300, 200, 'wheat')
    square(100, -100, 200, 'darkgray')
    square(100, 100, 200, 'hotpink')
    turtle.update()


def flash(tile):
    """Flash tile in grid."""
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    turtle.update()
    if len(pattern) > 5:
        sleep(0.4)
    elif len(pattern) > 10:
        sleep(0.3)
    elif len(pattern) > 15:
        sleep(0.2)
    else:
        sleep(0.5)
    square(tile.x, tile.y, 200, dark)
    turtle.update()
    if len(pattern) > 5:
        sleep(0.4)
    elif len(pattern) > 10:
        sleep(0.3)
    elif len(pattern) > 15:
        sleep(0.2)
    else:
        sleep(0.5)


def grow():
    """Grow pattern and flash tiles."""
    tile = choice(list(tiles))
    pattern.append(tile)

    print("\n\n\n\n\n\n\n\n\n\nNext round!")
    sleep(0.5)
    if len(pattern) == 6 or len(pattern) == 11 or len(pattern) == 16:
        print("Speed up!")
        sleep(1)
    print("Ready to flash the patterns in 3...")
    sleep(1)
    print("Ready to flash the patterns in 2...")
    sleep(1)
    print("Ready to flash the patterns in 1...")
    sleep(1)
    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()


def tap(x, y):
    """Respond to screen tap."""
    turtle.onscreenclick(None)
    x = floor(x, 100) 
    y = floor(y, 100) 
    if x % 200 == 0:
        x -= 100
    if y % 200 == 0:
        y -= 100
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        print("Opps! This is wrong!")
        exit()

    print("Correct!")
    

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    turtle.onscreenclick(tap)


def start(x, y):
    """Start game."""
    grow()
    turtle.onscreenclick(tap)


turtle.setup(750, 750, 100, 100)
turtle.hideturtle()
turtle.tracer(False)
grid()
turtle.onscreenclick(start)
turtle.done()
