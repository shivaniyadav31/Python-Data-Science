import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess the lucky number: "))

        if user_num == lucky_num:
            print("YOU WON.... Game over!!!")
            break
        elif user_num < lucky_num:
            print("Too low...")
        else: 
            print("Too high...")

    print("Thank You for playing.")

play_game()