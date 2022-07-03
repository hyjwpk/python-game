'''
This is the main function for the game choose.
'''
import os
import time
import random as rd
path = os.path.abspath('.')

gamelist = [
    'Ant',
    'Bagles',
    'Boom',
    'Bounce',
    'Cannon',
    'Connect',
    'Crypto',
    'Fidget',
    'Flappy',
    'Guess',
    'Life',
    'Madlibs',
    'Maze',
    'Memory',
    'Minesweeper',
    'Pacman',
    'Paint',
    'Pong',
    'Rps_game',
    'Simonsays',
    'Snake',
    'Tictactoe',
    'Tiles',
    'Tron',

]

def blank(num):
    for i in range(0, num):
        print(" ")

def info():     # print("")

    print("[Cannon]")
    print("    Projectile motion. Click the screen to fire your cannnonball. The")
    print("cannonball pops blue balloons in its path. Pop all the balloons before they can")
    print("cross the screen.")
    blank(1)

    print("[Connect]")
    print("    Connect 4 game. Click a row to drop a disc. The first player to")
    print("connect four discs vertically, horizontally, or diagonally wins!")
    blank(1)

    print("[Fidget]")
    print("     Fidget spinner inspired animation. Click the screen to accelerate")
    print("the fidget spinner.")
    blank(1)

    print("[Flappy]")
    print("    Flappy-bird inspired game. Click the screen to flap your")
    print("wings. Watch out for black ravens as you fly across the screen.")
    blank(1)

    print("[Life]")
    print("     Conway's Game of Life. The classic, zero-player, cellular automation")
    print("created in 1970 by John Conway.")
    blank(1)

    print("[Maze]")
    print("    Move from one side to another. Inspired by `A Universe in One Line")
    print("of Code with 10 PRINT`_. Tap the screen to trace a path from one side to")
    print("another.")
    blank(1)

    print("[Memory]")
    print("    Puzzle game of number pairs. Click a tile to reveal a")
    print("number. Match two numbers and the tiles will disappear to reveal an image.")
    blank(1)
    
    print("[Pacman]")
    print("    Classic arcade game. Use the arrow keys to navigate and eat all")
    print("the white food. Watch out for red ghosts that roam the maze.")
    blank(1)

    print("[Paint]")
    print("    Draw lines and shapes on the screen. Click to mark the start of a")
    print("shape and click again to mark its end. Different shapes and colors can be")
    print("selected using the keyboard.")
    blank(1)

    print("[Pong]")
    print("    Classic arcade game. Use the keyboard to move your paddle up and")
    print("down. The first player to miss the ball loses.")
    blank(1)
    
    print("[Simon Says]")
    print("    Classic memory puzzle game. Click the screen to start. Watch")
    print("the pattern and then click the tiles in the same order. Each time you get the")
    print("sequence right the pattern gets one step longer.")
    blank(1)

    print("[Snake]")
    print("    Classic arcade game. Use the arrow keys to navigate and eat the")
    print("green food. Each time the food is consumed, the snake grows one segment")
    print("longer. Avoid eating yourself or going out of bounds!")
    blank(1)

    print("[Tic Tac Toe]")
    print("    Classic game. Click the screen to place an X or O. Connect")
    print("three in a row and you win!")
    blank(1)

    print("[Tiles]")
    print("    Puzzle game of sliding numbers into place. Click a tile adjacent to")
    print("the empty square to swap positions. Can you make the tiles count one to fifteen")
    print("from left to right and bottom to top?")
    blank(1)

    print("[Tron]")
    print("    Classic arcade game. Use the keyboard to change the direction of")
    print("your Tron player. Avoid touching the line drawn by your opponent.")
    blank(1)


# MAIN function starts here

blank(100)
print("Welcome to Free-Python-Games.")
print("This project is adapted from github project [free-pythpn-game].")
print("Website: http://www.grantjenks.com/docs/freegames/")
print("This project is ONLY for the course <Interdisciplinary Python Programming and Interdisciplinary Practice>")
print("Now, enjoy the game!")
blank(5)

while True:
    print("Play something, have a rest~")
    print("[List]           [Info]          [Random]         [Exit]")
    choice = input("[Input]:").upper()
    blank(10)

    if choice == 'EXIT':
        print("See you later ~ Goodbye!")
        time.sleep(1)
        exit()
    elif choice == 'INFO':
        print("The game introduction is as below.")
        print("========================================================")
        info()
        blank(3)
    elif choice == 'LIST':
        print("     ================================   GAME LIST   ======================================")
        for i in range(0, len(gamelist)) :
            print("     {}.[{}]     ".format(i + 1, gamelist[i]), end="")
            if i % 5 == 4:
                blank(1)
        print("\n     =====================================================================================")

        print("\n\nPlease input the number to play the game.")
        print("Input 0 for quit.")
        num = int(input("[input]:"))
        if num < 0 or num > len(gamelist):
            num = 0
        if num == 0:
            blank(5)
            continue
        name = '/' + gamelist[num - 1].lower() + '.py'
        os.system('python ' + path + name)
        blank(10)
    elif choice == 'RANDOM':
        num = rd.randint(1, len(gamelist))
        print("This game is: {}".format(gamelist[num - 1]))
        time.sleep(1)
        print("The game will start in 3...")
        time.sleep(1)
        print("The game will start in 2...")
        time.sleep(1)
        print("The game will start in 1...")
        time.sleep(1)
        name = '/' + gamelist[num - 1].lower() + '.py'
        os.system('python ' + path + name)
        blank(10)