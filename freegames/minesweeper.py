"""Minesweeper

Exercises

1. What does the `seed(0)` function call do?
2. Change the number of bombs on the grid.
3. Change the size of the grid.
"""

from random import randrange, seed
import turtle
from utils import floor, square

seed(0)
bombs = {}
shown = {}
counts = {}


def initialize():
    """Initialize `bombs`, `counts`, and `shown` grids."""
    for x in range(-250, 250, 50):
        for y in range(-250, 250, 50):
            bombs[x, y] = False
            shown[x, y] = False
            counts[x, y] = -1

    for count in range(8):
        x = randrange(-200, 200, 50)
        y = randrange(-200, 200, 50)
        bombs[x, y] = True

    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            total = 0
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    total += bombs[x + i, y + j]
            counts[x, y] = total


def stamp(x, y, text):
    """Display `text` at coordinates `x` and `y`."""
    square(x, y, 50, 'white')
    turtle.color('black')
    turtle.write(text, font=('Arial', 50, 'normal'))


def draw():
    """Draw the initial board grid."""
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            stamp(x, y, '?')


def end():
    """Draw the bombs as X's on the grid."""
    for x in range(-200, 200, 50):
        for y in range(-200, 200, 50):
            if bombs[x, y]:
                stamp(x, y, 'X')


def tap(x, y):
    """Respond to screen click at `x` and `y` coordinates."""
    x = floor(x, 50)
    y = floor(y, 50)

    if bombs[x, y]:
        end()
        return

    pairs = [(x, y)]

    while pairs:
        x, y = pairs.pop()
        stamp(x, y, counts[x, y])
        shown[x, y] = True

        if counts[x, y] == 0:
            for i in (-50, 0, 50):
                for j in (-50, 0, 50):
                    pair = x + i, y + j
                    if not shown[pair]:
                        pairs.append(pair)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
initialize()
draw()
turtle.onscreenclick(tap)
turtle.done()
