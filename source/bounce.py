"""Bounce, a simple animation demo.

Exercises

1. Make the ball speed up and down.
2. Change how the ball bounces when it hits a wall.
3. Make the ball leave a trail.
4. Change the ball color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""

import random
import turtle
from utils import vector


def value():
    """Randomly generate value between (-5, -3) or (3, 5)."""
    return (3 + random.random() * 2) * random.choice([1, -1])


ball = vector(0, 0)
aim = vector(value(), value())


def draw():
    """Move ball and draw game."""
    ball.move(aim)

    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x

    if y < -200 or y > 200:
        aim.y = -aim.y

    # turtle.pendown()
    # turtle.color("red")
    # turtle.width(2)
    turtle.clear()
    turtle.goto(x, y)
    turtle.dot(10)

    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.up()
draw()
turtle.done()
