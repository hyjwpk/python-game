"""Ant, simple animation demo.
# Improved
Exercises

1. Wrap ant around screen boundaries.
2. Make the ant leave a trail.
3. Change the ant color based on position.
   Hint: colormode(255); color(0, 100, 200)
"""

import random
import turtle
from utils import vector

ant = vector(0, 0)
aim = vector(2, 0)


def wrap(value):
    """Wrap value around -200 and 200."""
    if value >= 300:
        value = 300
    elif value <= -300:
        value = -300
    return value  # TODO


def draw():
    """Move ant and draw screen."""
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)

# aturtle.pendown()   移动时绘制图形
# turtle.goto(x,y)    将画笔移动到坐标为x,y的位置
    aim.move(random.random() * 0.5 - 0.25)
    if ant.x >= 300 or ant.x <= -300 or ant.y >= 300 or ant.y <= -300:
        aim.rotate(90)
    else:
        aim.rotate(random.random() * 40 - 20)

    # turtle.clear()
    turtle.pendown()
    turtle.color("red")
    turtle.goto(ant.x, ant.y)
    turtle.color("black")
    turtle.dot(3)

    turtle.ontimer(draw, 80)


# turtle.setup(420, 420, 370, 0)
turtle.setup(800, 800, 370, 0)
turtle.hideturtle()
turtle.title("Ant Simulater")
turtle.tracer(False)
turtle.up()

turtle.penup()
turtle.color("blue")
turtle.goto(300, -300)
turtle.left(90)
turtle.pendown()
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.left(90)
turtle.forward(600)
turtle.penup()
turtle.home()

draw()
turtle.done()
