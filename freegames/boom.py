'''
The number guess game, but for 2 players!
Players will guess the number in turn
Anyone guesses the number first will LOSE
'''

import random as rd
import time
start = 1
end = 100
player = 1
playernum = int(input("Please input the number of players (MAX 4)\n[input]:"))
if playernum < 0:
    playernum = 1
elif playernum > 4:
    playernum = 4

value = rd.randint(start, end)

while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n=====================================================")
    print("This is player {}'s round.".format(player))
    print("Choose a number between {} and {}.".format(start, end))
    while True:
        guess = int(input("[input]:"))
        if guess >= start and guess <= end:
            break
        print("Out of range. Please choose another number.")
    time.sleep(1)
    

    if guess == value:
        print("Ssssssssssss....")
        time.sleep(1)
        print("Boom!")
        time.sleep(1)
        print("Player {} was blown up, game over.".format(player))
        exit()
    elif guess < value:
        print("Not this one. It's bigger.")
        start = guess + 1
    else:
        print("Not this one. It's smaller.")
        end = guess - 1
    time.sleep(2)

    # Change the player
    if player >= playernum:
        player = 1
    else:
        player += 1