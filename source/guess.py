"""Guess a number within a range.

Exercises

1. Change the range to be from 0 to 1,000,000.
2. Can you still guess the number?
3. Print the number of guesses made.
4. Limit the number of guesses to the minimum required.
"""

from random import randint

start = 1
end = 100
value = randint(start, end)

# print(value)
print("I'm thinking of a number between", start, 'and', end)
T = int(input("Please input the honesty percent (From 0 to 100):\n[input]:"))
if T < 0:
    T = 0
elif T > 100:
    T = 100

guess = None

while guess != value:
    text = input('Guess the number: ')
    guess = int(text)

    flag = randint(1,100)
    if flag < T:
        if guess < value:
            print('Higher.')
        elif guess > value:
            print('Lower.')
    else:
        if guess < value:
            print('Lower.')
        elif guess > value:
            print('Higher.')

print('Congratulations! You guessed the right answer:', value)
