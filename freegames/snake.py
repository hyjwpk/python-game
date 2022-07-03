"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from tkinter.tix import Tree
import turtle
import time
from utils import vector


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
game_on = 1

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def stop():
    global game_on 
    if game_on == 1:
        game_on = 0
    else:
        game_on = 1


def square(x, y, size, name):
    """
    Draw square at `(x, y)` with side length `size` and fill color `name`.

    The square is oriented so the bottom left corner is at (x, y).

    """
    import turtle

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(name)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def across(head):
    '''Make the head jump across the boundaries.'''
    if head.x < -200:
        head.x = 190
        return
    if head.x > 190:
        head.x = -200
        return
    if head.y < -200:
        head.y = 190
        return
    if head.y > 190:
        head.y = -200
        return


def move():
    global game_on

    if game_on == 1:
        """Move snake forward one segment."""
        head = snake[-1].copy()
        head.move(aim)

        across(head)
        # if not inside(head) or head in snake:
        if head in snake:
            square(head.x, head.y, 9, 'red')
            turtle.update()
            return

        snake.append(head)

        if head == food:
            print('Snake:', len(snake))
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
        else:
            snake.pop(0)

        turtle.clear()

        for body in snake:
            square(body.x, body.y, 9, 'black')

        square(food.x, food.y, 9, 'green')
        turtle.update()

    turtle.ontimer(move, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
move()
 
turtle.onkey(lambda: change(10, 0), 'Right')
turtle.onkey(lambda: change(-10, 0), 'Left')
turtle.onkey(lambda: change(0, 10), 'Up')
turtle.onkey(lambda: change(0, -10), 'Down')
turtle.onkey(lambda: stop(), 'space')
    # time.sleep(0.1)
    # move()

turtle.done()
print(2)