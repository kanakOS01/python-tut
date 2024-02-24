import random
from words import words
import string
from visual import lives_visual_dict

def get_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    lives = 7

    word = get_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    guessed_letters = set() # letters guessed by the user

    # user input
    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left.")
        print(lives_visual_dict[7 - lives])
        print("You have used these letters - " + ' '.join(guessed_letters))
        # print the current word
        guessed_word = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current Word - " + ' '.join(guessed_word))

        user_input = input("Guess the letter : ").upper()
        if (user_input not in alphabet):
            print("Enter valid character.")
        elif (user_input in (alphabet - guessed_letters)):
            guessed_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
                print("Letter not in word")
        elif user_input in guessed_letters:
            print("You have already guessed that character.")
    
    if lives == 0:
        print("You have died.")
    else:
        print("You win.")
    
    print(f"The word was \033[1;32m{word.upper()}\033[0m")

hangman()
