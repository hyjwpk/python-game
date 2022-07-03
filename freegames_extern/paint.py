"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

# from turtle import *
import turtle
import math
from freegames import vector


def line(start, middle, end):
    """Draw line from start to end."""

    turtle.goto(end.x, end.y)


def square(start, middle, end):
    """Draw square from start to end."""
    for count in range(4):
        turtle.forward(end.x - start.x)
        turtle.left(90)


def circle(start, middle, end):
    """Draw circle from start to end."""
    r = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5
    angle = math.atan2(end.x - start.x, end.y - start.y)
    angle = int(angle * 180/math.pi)
    turtle.right(angle)
    turtle.circle(r)
    turtle.left(angle)
    pass  # TODO


def rectangle(start, middle, end):
    """Draw rectangle from start to end."""

    turtle.forward(end.x - start.x)
    turtle.left(90)
    turtle.forward(end.y - start.y)
    turtle.left(90)
    turtle.forward(end.x - start.x)
    turtle.left(90)
    turtle.forward(end.y - start.y)
    turtle.left(90)
    pass  # TODO


def triangle(start, middle, end):
    """Draw triangle from start to end."""
    turtle.goto(middle.x, middle.y)
    turtle.goto(end.x, end.y)
    turtle.goto(start.x, start.y)
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']
    middle = state['middle']
    shape = state['shape']

    if state['shape'] != triangle:
        if start is None:
            state['start'] = vector(x, y)
        else:
            shape = state['shape']
            end = vector(x, y)
            draw_shape(start, middle, end)
            state['start'] = None
    else:
        if start is None:
            state['start'] = vector(x, y)
        elif middle is None:
            state['middle'] = vector(x, y)
        else:
            shape = state['shape']
            end = vector(x, y)
            draw_shape(start, middle, end)
            state['start'] = None
            state['middle'] = None


def draw_shape(start, middle, end):
    turtle.up()
    turtle.goto(start.x, start.y)
    turtle.down()
    shape = state['shape']
    if state['fill'] == 'yes':
        turtle.begin_fill()

    shape(start, middle, end)

    if state['fill'] == 'yes':
        turtle.end_fill()


def store(key, value):
    """Store value in state at key."""
    state[key] = value


def main():
    #state = {'start': None, 'middle': None, 'shape': line, 'fill': 'no'}
    turtle.setup(420, 420, 370, 0)
    turtle.onscreenclick(tap)
    turtle.listen()
    turtle.onkey(turtle.undo, 'u')
    turtle.onkey(lambda: turtle.color('black'), 'K')
    turtle.onkey(lambda: turtle.color('white'), 'W')
    turtle.onkey(lambda: turtle.color('green'), 'G')
    turtle.onkey(lambda: turtle.color('blue'), 'B')
    turtle.onkey(lambda: turtle.color('red'), 'R')
    turtle.onkey(lambda: store('shape', line), 'l')
    turtle.onkey(lambda: store('shape', square), 's')
    turtle.onkey(lambda: store('shape', circle), 'c')
    turtle.onkey(lambda: store('shape', rectangle), 'r')
    turtle.onkey(lambda: store('shape', triangle), 't')
    turtle.onkey(lambda: store('fill', 'yes'), 'f')
    turtle.onkey(lambda: store('fill', 'no'), 'F')
    turtle.done()


state = {'start': None, 'middle': None, 'shape': line, 'fill': 'no'}

if __name__ == '__main__':

    main()
