# computer will generate a random number and we will guess the number

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while (random_number != guess):
        guess = int(input(f"Enter your guess between 1 and {x}: "))
        if (guess == random_number):
            print("Congratulations. You have guessed the number correctly")
        elif (guess < random_number):
            print("Your guess is too low")
        elif (guess > random_number):
            print("Your guess is too high")
    
guess(10)
