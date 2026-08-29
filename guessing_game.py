import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = input("Guess the lucky number")

        if user_num == luvky_num