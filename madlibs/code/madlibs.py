# What is madlibs
# Word game in which u put random words in the blanks without any context and then you get an amusing result, which may be nonsensical and funny.

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# madlib = f"Computer programming is so \033[3;91m{adj}\033[0m! It makes me so excited all the time because I love to \033[3;91m{verb1}\033[0m. Stay hydrated and \033[3;91m{verb2}\033[0m like you are \033[3;91m{famous_person}\033[0m"

# print(madlib)

# -----------------
# Random madlib game
from samples import zombie, birthday, sports, exam
import random

if __name__ == "__main__":
    choice = random.choice([zombie, birthday, sports, exam])
    choice.madlib()