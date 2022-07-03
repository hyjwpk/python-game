"""Maze, move from one side to another.

Excercises

1. Keep score by counting taps.
2. Make the maze harder.
3. Generate the same maze twice.
"""

from random import random
import turtle
from utils import line


def draw():
    """Draw maze."""
    turtle.color('black')
    turtle.width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    turtle.update()


def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:
        turtle.up()
    else:
        turtle.down()

    turtle.width(2)
    turtle.color('red')
    turtle.goto(x, y)
    turtle.dot(4)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
draw()
turtle.onscreenclick(tap)
turtle.done()
