import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"
check = True
while check:
    number = 5
    guess = input("Guess a number from 1 to 10: ")
    if guess.isdigit():
        if 1 <= int(guess) <= 10:
            check = False

if guess == number:
    print("Great job! You got it!")
else:
    print("Sorry, better luck next time.")
    print("The number was " + str(number))
