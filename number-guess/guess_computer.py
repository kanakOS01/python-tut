# we have a number and the computer has to guess it correctly

import random

def guess(l, h):
    print(f"Think of a number between {l} and {h} both inclusive")
    print("I will now start guessing the number.")
    print("You need to print \033[3;91m'low'\033[0m if the guess is too low, \033[3;91m'high'\033[0m if the number is too high, or \033[3;91m'correct'\033[0m if it is correct")
    guess = 0
    feedback = ''
    s = l
    e = h

    while (s <= e):
        guess = random.randint(s, e)
        print("My guess is " + str(guess))

        feedback = input().lower()

        if (feedback == 'low'):
            s = guess + 1
        elif (feedback == 'high'):
            e = guess - 1
        elif (feedback == 'correct'):
            break
        else:
            print("Wrong feedback")

    if (feedback == 'correct'):
        print("Yay I won")
    else:
        print("Are you sure you are not cheating??")

guess(10, 20)