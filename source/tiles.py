"""Tiles, number swapping game.

Exercises

1. Track a score by the number of tile moves.
2. Permit diagonal squares as neighbors.
3. Respond to arrow keys instead of mouse clicks.
4. Make the grid bigger.
"""

import random
import turtle

from utils import floor, vector

tiles = {}
neighbors = [
    vector(100, 0),
    vector(-100, 0),
    vector(0, 100),
    vector(0, -100),
]

writer = turtle.Turtle(visible=False)
count = 0

def load():
    """Load tiles and scramble."""
    count = 1

    for y in range(-200, 200, 100):
        for x in range(-200, 200, 100):
            mark = vector(x, y)
            tiles[mark] = count
            count += 1

    tiles[mark] = None

    for count in range(1000):
        neighbor = random.choice(neighbors)
        spot = mark + neighbor

        if spot in tiles:
            number = tiles[spot]
            tiles[spot] = None
            tiles[mark] = number
            mark = spot


def square(mark, number):
    """Draw white square with black outline and number."""
    turtle.up()
    turtle.goto(mark.x, mark.y)
    turtle.down()

    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(99)
        turtle.left(90)
    turtle. end_fill()

    if number is None:
        return
    elif number < 10:
        turtle.forward(20)

    turtle.write(number, font=('Arial', 60, 'normal'))


def tap(x, y):
    global count
    """Swap tile and empty square."""
    x = floor(x, 100)
    y = floor(y, 100)
    mark = vector(x, y)

    count += 1

    writer.undo()
    writer.goto(260, 160)
    writer.color('black')
    writer.write(count)

    for neighbor in neighbors:
        spot = mark + neighbor

        if spot in tiles and tiles[spot] is None:
            number = tiles[mark]
            tiles[spot] = number
            square(spot, number)
            tiles[mark] = None
            square(mark, None)


def draw():
    """Draw all tiles."""
    for mark in tiles:
        square(mark, tiles[mark])
    turtle.update()


turtle.setup(600, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
load()
draw()
turtle.onscreenclick(tap)
turtle.done()


