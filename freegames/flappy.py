"""Flappy, game inspired by Flappy Bird.

Exercises

1. Keep score.
2. Vary the speed.
3. Vary the size of the balls.
4. Allow the bird to move forward and back.
"""

import random
import turtle
from utils import vector

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 50)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    turtle.clear()

    turtle.goto(bird.x, bird.y)

    if alive:
        turtle.dot(10, 'green')
    else:
        turtle.dot(10, 'red')

    for ball in balls:
        turtle.goto(ball.x, ball.y)
        turtle.dot(20, 'black')

    turtle.update()


def move():
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if random.randrange(10) == 0:
        y = random.randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    turtle.ontimer(move, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.up()
turtle.tracer(False)
turtle.onscreenclick(tap)
move()
turtle.done()
