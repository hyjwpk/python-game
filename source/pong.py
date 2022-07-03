"""Pong, classic arcade game.

Exercises

1. Change the colors.
2. What is the frame rate? Make it faster or slower.
3. Change the speed of the ball.
4. Change the size of the paddles.
5. Change how the ball bounces off walls.
6. How would you add a computer player?
6. Add a second ball.
"""

from random import choice, random
import turtle
from utils import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random() * 2) * choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}


def move(player, change):
    """Move player position by change."""
    state[player] += change


def rectangle(x, y, width, height):
    """Draw rectangle at (x, y) with given width and height."""
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    for count in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw():
    """Draw game and move pong ball."""
    turtle.clear()
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    turtle.up()
    turtle.goto(x, y)
    turtle.dot(10)
    turtle.update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50

        if low <= y <= high:
            aim.x = -aim.x
        else:
            return

    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: move(1, 20), 'w')
turtle.onkey(lambda: move(1, -20), 's')
turtle.onkey(lambda: move(2, 20), 'i')
turtle.onkey(lambda: move(2, -20), 'k')
draw()
turtle.done()
