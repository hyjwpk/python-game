"""Tron, classic arcade game.

Exercises

1. Make the tron players faster/slower.
2. Stop a tron player from running into itself.
3. Allow the tron player to go around the edge of the screen.
4. How would you create a computer player?
"""

import turtle

from utils import square, vector

p1xy = vector(-100, 0)
p1aim = vector(4, 0)
p1body = set()

p2xy = vector(100, 0)
p2aim = vector(-4, 0)
p2body = set()

def change(aim, x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside screen."""
    return -200 < head.x < 200 and -200 < head.y < 200

def across(head):
    '''Make the head jump across the boundaries.'''
    if head.x < -200:
        head.x = 200
        return
    if head.x > 200:
        head.x = -200
        return
    if head.y < -200:
        head.y = 200
        return
    if head.y > 200:
        head.y = -200
        return


def draw():
    """Advance players and draw game."""
    p1xy.move(p1aim)
    across(p1xy)
    
    p1head = p1xy.copy()

    p2xy.move(p2aim)
    across(p2xy)

    p2head = p2xy.copy()
    
    
    if p1head in p2body:
        print('Player red wins!')
        return

    if p2head in p1body:
        print('Player blue wins!')
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1xy.x, p1xy.y, 3, 'blue')
    square(p2xy.x, p2xy.y, 3, 'red')
    turtle.update()
    turtle.ontimer(draw, 50)


turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
turtle.listen()

turtle.onkey(lambda: change(p1aim, 4, 0), 'Right')
turtle.onkey(lambda: change(p1aim, -4, 0), 'Left')
turtle.onkey(lambda: change(p1aim, 0, 4), 'Up')
turtle.onkey(lambda: change(p1aim, 0, -4), 'Down')

turtle.onkey(lambda: change(p2aim, 4, 0), 'd')
turtle.onkey(lambda: change(p2aim, -4, 0), 'a')
turtle.onkey(lambda: change(p2aim, 0, 4), 'w')
turtle.onkey(lambda: change(p2aim, 0, -4), 's')

draw()
turtle.done()
