"""Game of Life simulation.

Conway's game of life is a classic cellular automation created in 1970 by John
Conway. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

A special website simulator: https://funnyjs.com/jspages/game-of-life.html

Exercises

1. Can you identify any Still Lifes, Oscillators, or Spaceships?
2. How can you make the simulation faster? Or bigger?
3. How would you modify the initial state?
4. Try changing the rules of life :)
"""

from random import choice
import turtle
from utils import square

cells = {}


def initialize(mode = "random"):
    """initialize the cells according to the modes."""
    
    for x in range(-200, 200, 10):
        for y in range(-200, 200, 10):
            cells[x, y] = False

    if mode == "random" or mode == "none":
        for x in range(-50, 50, 10):
            for y in range(-50, 50, 10):
                cells[x, y] = choice([True, False])
    
    elif mode == "comb":
        cells[0, 0] = True
        cells[10, 0] = True
        cells[20, 10] = True
        cells[10, 20] = True
        cells[0, 20] = True
        cells[-10, 10] = True

    elif mode == "boat":
        cells[0, -10] = True
        cells[10, -10] = True
        cells[-10, 0] = True
        cells[10, 0] = True
        cells[-10, 10] = True
        cells[0, 10] = True

    elif mode == "star":
        cells[-40, -60] = True
        cells[-30, -60] = True
        cells[-20, -60] = True
        cells[40, -60] = True
        cells[30, -60] = True
        cells[20, -60] = True

        cells[-60, -40] = True
        cells[-10, -40] = True
        cells[60, -40] = True
        cells[10, -40] = True

        cells[-60, -30] = True
        cells[-10, -30] = True
        cells[60, -30] = True
        cells[10, -30] = True

        cells[-60, -20] = True
        cells[-10, -20] = True
        cells[60, -20] = True
        cells[10, -20] = True

        cells[-40, -10] = True
        cells[-30, -10] = True
        cells[-20, -10] = True
        cells[40, -10] = True
        cells[30, -10] = True
        cells[20, -10] = True

        cells[-40, 60] = True
        cells[-30, 60] = True
        cells[-20, 60] = True
        cells[40, 60] = True
        cells[30, 60] = True
        cells[20, 60] = True

        cells[-60, 40] = True
        cells[-10, 40] = True
        cells[60, 40] = True
        cells[10, 40] = True

        cells[-60, 30] = True
        cells[-10, 30] = True
        cells[60, 30] = True
        cells[10, 30] = True

        cells[-60, 20] = True
        cells[-10, 20] = True
        cells[60, 20] = True
        cells[10, 20] = True

        cells[-40, 10] = True
        cells[-30, 10] = True
        cells[-20, 10] = True
        cells[40, 10] = True
        cells[30, 10] = True
        cells[20, 10] = True

    elif mode == "spaceship":
        cells[-150, -20] = True
        cells[-140, -20] = True
        cells[-130, -20] = True
        cells[-120, -20] = True

        cells[-160, -10] = True
        cells[-120, -10] = True

        cells[-120, 0] = True
        cells[-160, 10] = True
        cells[-130, 10] = True

    else:
        print("Mode error!")
        cells[10, 10] = True
        cells[0, 0] = True
        cells[10, 0] = True
        cells[0, 10] = True

def step():
    """Compute one step in the Game of Life."""
    neighbors = {}

    for x in range(-190, 190, 10):
        for y in range(-190, 190, 10):
            count = -cells[x, y]
            for h in [-10, 0, 10]:
                for v in [-10, 0, 10]:
                    count += cells[x + h, y + v]
            neighbors[x, y] = count

    for cell, count in neighbors.items():
        if cells[cell]:
            if count < 2 or count > 3:
                cells[cell] = False
        elif count == 3:
            cells[cell] = True


def draw():
    """Draw all the squares."""
    step()
    turtle.clear()
    for (x, y), alive in cells.items():
        color = 'green' if alive else 'black'
        square(x, y, 10, color)
    turtle.update()
    
    draw()
    turtle.ontimer(draw, 100)



print("Pleast input the initial mode:\n    <none>/<random>: Randomly initialize.\n    <comb>: A honeycomb shape (static)\n    <boat>: A small boat (static)")
print("    <star>: A cycle change star. (dynamic)")
print("    <spaceship>: A spaceship which can move. (dynamic)")
mode = input("\n[input]:")
if mode == "":
    mode = "random"

turtle.setup(420, 420, 370, 0)
turtle.hideturtle()
turtle.tracer(False)
initialize(mode)
draw()
turtle.done()

