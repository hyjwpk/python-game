# rock paper scissors!

import random, time

game_count = 0
win = 0
lose = 0
draw = 0
print("Welcome to Rock-Paper-Scissors Game!")
total = int(input("Please input the total game rounds (odd):\n[input]:"))
if total % 2 == 0:
    total = total + 1

while game_count < total:
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n=============================================================")
    print("\nRound {} / {}".format(game_count + 1, total))

    while True:
        player = (input("Please make your choice: Rock、 Papar or Scissors\n")).upper()
        if player == "R":
            player = "ROCK"
        if player == "P":
            player = "PAPER"
        if player == "S":
            player = "SCISSORS"
        if player == "ROCK" or player == "PAPER" or player == "SCISSORS":
            break
        print("You can't choose that. Try again.")


    choice = ["PAPER", "ROCK", "SCISSORS"]
    computer = choice[random.randint(0, 2)]

    print("Your choice was: {}, while computer chose {}.".format(player, computer))
    if player == computer:
        draw += 1
        print("This is a draw!")
        
    elif (player == "ROCK" and computer == "PAPER") or (player == "PAPER" and computer == "SCISSORS") or (player == "SCISSORS" and computer == "ROCK"):
        lose += 1
        print("Opps, you lose.")
        
    else:
        win += 1
        print("Great! You got it!")
    time.sleep(0.5)
    game_count += 1

    if lose == (total + 1) // 2 or win == (total + 1) // 2:      
        break

print("\n\n=============================================================")
print("Results:")
print("    win --- {} times".format(win))
print("    lose --- {} times".format(lose))
print("    draw --- {} times".format(draw))
print("    total --- {} times".format(game_count))
print("=============================================================\n")
if lose > win:
    print("You lose. Maybe next time will be better.")
elif lose < win:
    print("You win! Congratulations!")
else:
    print("Just soso.")
print("\n\n")