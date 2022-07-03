"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?
"""

"""
Improve:

1. Add the class for players
2. Detect a winner
3. Add logic to detect a full row.
"""

import turtle
import time
from utils import line



class Player(object):
    def __init__(self, color):
        self.color = color

    def change_color(self, color_new):
        self.color = color_new


game_state = [[[0 for i in range (9)] for _ in range(8)] for _ in range(8)]

# This array stores the number of points in different ways.
# 0 --- player number 0 or 1
# 1 --- up
# 2 --- up and left
#       ...
# 8 --- up and right

offset = [[0] * 2 for _ in range (8)]
offset[0] = [0, 1]
offset[1] = [-1, 1]
offset[2] = [-1, 0]
offset[3] = [-1, -1]
offset[4] = [0, -1]
offset[5] = [1, -1]
offset[6] = [1, 0]
offset[7] = [1, 1]

current_id = 1

def winner_detect(row, col, player_id):
    global game_state, offset, current_id


    game_state[row][col][0] = player_id

    for i in range(0, 8):
        check_row = row + offset[i][0]
        check_col = col + offset[i][1]
        # Detect the edge
        if check_row < 0 or check_row > 7 or check_col < 0 or check_col > 7:
            continue

        if game_state[row][col][0] == game_state[check_row][check_col][0]:
            game_state[row][col][i + 1] = game_state[check_row][check_col][i + 1] + 1
            game_state[check_row][check_col][(i + 4) % 8 + 1] = game_state[row][col][(i + 4) % 8 + 1] + 1
            if game_state[row][col][i + 1] >= 3:
                print("Braveo!")
                time.sleep(0.5)
                print("Player " + str(player_id), end= " ")
                print("Win!") 
                time.sleep(2)
                print("The game will end in 3...")
                time.sleep(1)
                print("The game will end in 2...")
                time.sleep(1)
                print("The game will end in 1...")
                time.sleep(1)
                exit()


turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def grid():
    """Draw Connect Four grid."""
    turtle.bgcolor('light blue')

    for x in range(-200, 250, 50):
        line(x, -200, x, 200)
        line(-200, x, 200, x)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            turtle.up()
            turtle.goto(x, y)
            turtle.dot(40, 'white')

    turtle.update()


def tap(x, y):
    """Draw red or yellow circle in tapped row."""
    global current_id

    player = state['player']
    rows = state['rows']

    col = int((x + 200) // 50)
    if col < 0 or col > 7:
        print("Out of the ground!")
        return
    count = rows[col]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    

    if y > 200:
        print("This colmun is full!")
        print("Please try another place")
        return

    turtle.up()
    turtle.goto(x, y)
    turtle.dot(40, player)
    turtle.update()

    rows[col] = count + 1
    state['player'] = turns[player]

    md_row = int((x + 175) // 50)
    md_col = 7 - int((y + 175) // 50)

    # print(md_row)
    # print(md_col)

    # winner_detect(md_row, md_col, current_id)

    # print(current_id)
    player_id = current_id
    winner_detect(md_row, md_col, player_id)
    if current_id == 1:
        current_id = 2
    else:
        current_id = 1

# Begins from now
turtle.setup(500, 500, 370, 0)
turtle.hideturtle()
turtle.tracer(False)


# Game start
# Player 0 starts first
grid()
turtle.onscreenclick(tap)
turtle.done()
