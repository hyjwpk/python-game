"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.
"""

import turtle
state = {'turn': 0}


def spinner():
    """Draw fidget spinner."""
    turtle.clear()
    angle = state['turn'] / 10
    turtle.right(angle)
    turtle.forward(100)
    turtle.dot(120, 'red')
    turtle.back(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'green')
    turtle.back(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.dot(120, 'blue')
    turtle.back(100)
    turtle.right(120)
    turtle.update()


def animate():
    """Animate fidget spinner."""
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    turtle.ontimer(animate, 20)


def flick():
    """Flick fidget spinner."""
    state['turn'] += 10


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.width(20)
turtle.onkey(flick, 'space')
turtle.listen()
animate()
turtle.done()
