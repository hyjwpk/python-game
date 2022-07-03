from random import randrange
from turtle import *
import sys

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
running = 1


def change(x, y):
    """Change snake direction."""
    if x != 0 and aim.x != 0 and x + aim.x == 0:
        return
    elif y != 0 and aim.y != 0 and y + aim.y == 0:
        return
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    if head.x <= -200:
        head.x = 190
    elif head.x >= 190:
        head.x = -200
    elif head.y <= -200:
        head.y = 190
    elif head.y >= 190:
        head.y = -200
    return -200 <= head.x <= 190 and -200 <= head.y <= 190


def direction(key):
    if aim.x != -10 and key == 'Right':
        change(10, 0)
    if aim.x != 10 and key == 'Left':
        change(-10, 0)
    if aim.y != -10 and key == 'Up':
        change(0, 10)
    if aim.y != 10 and key == 'Down':
        change(0, -10)


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        print(running)
        ontimer(restart(), 100)
        return

    snake.append(head)
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


def restart():
    print('tape r to restart;tape q to exit')
    listen()
    onkey(main, 'r')
    onkey(exit, 'q')


def exit():
    sys.exit()


def main():
    setup(420, 420, 370, 0)
    if len(snake) > 1:
        for body in range(len(snake) - 1):
            snake.pop(0)
    reset()
    hideturtle()
    tracer(False)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()


if __name__ == '__main__':
    main()
