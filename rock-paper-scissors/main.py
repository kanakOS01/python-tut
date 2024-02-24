import random

def play():
    print("Lets play rock paper scissors")
    print("You and I have choose from \033[1;91m'R'\033[0m, \033[1;91m'P'\033[0m, \033[1;91m'S'\033[0m")
    print("Enter you choice when told to")
    print("It is a match till 3")
    print("Lets start")
    list = ['r', 'p', 's']
    comp_guess = ''
    user_guess = ''
    comp_score = 0
    user_score = 0

    while (user_score < 3 and comp_score < 3):
        print("\033[1;34mRock Paper Scissor, SHOOT!!\033[0m")
        user_guess = input("You threw - ").lower()
        comp_guess = random.choice(list)
        print(f"Computer threw - {comp_guess}")

        if (user_guess == comp_guess):
            print("It's a tie!")
        elif (is_win(comp_guess, user_guess)):
            print("Computer wins!")
            comp_score += 1
        else:
            print("Your win!")
            user_score += 1

        print(f"User Score : {user_score}")
        print(f"Computer Score : {comp_score}")

    if (user_score == 3):
        print("\033[1;32mYou are a tough player huh. You win !!!\033[0m")
    else:
        print("\033[1;32mBetter luck next time. You lose !!!\033[0m")

def is_win(a, b):
    if (a == 'r' and b == 's') or (a == 's' and b == 'p') or (a == 'p' and b == 'r'):
       return True
    
play()