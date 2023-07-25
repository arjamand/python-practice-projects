# 2022-10-31 15:36:11

# Guess the number game


import random
from art import logo
print(logo)
HARD_COUNT = 5
EASY_COUNT = 10
print("Welcome to number guessing game .\nI am thinking of a number between 1 and 100 ")

d_level = (input("Choose the dificulty level \"easy\" or \"hard\" : ")).lower()

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
          53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

guess_number = (random.choice(number))
# for x in range(101):
#     data.append(x)


def easy():
    """Changing the attempts according to the easy level .
    if the 'd_level' input is equal to 'easy' """
    # signal = True
    EASY_COUNT = 10
    while EASY_COUNT != 0:
        Guess = int(
            input(f"\nYou have {EASY_COUNT} attempts left .\nGuess the number : "))
        if Guess == guess_number:
            print(
                f"You guessed the number correct , it was {guess_number} !!! ")
            EASY_COUNT = 0
        elif Guess != guess_number and EASY_COUNT != 1:
            if Guess > guess_number:
                print("Too high , try again .")
                EASY_COUNT -= 1
            elif Guess < guess_number:
                print("Too low, try again .")
                EASY_COUNT -= 1
        elif Guess != guess_number and EASY_COUNT == 1:
            print(f"You lost , the number to guess was {guess_number} .")


def hard():
    """Changing the attempts according to the hard level .
    if the 'd_level' input is equal to 'hard' """
    HARD_COUNT = 5
    while HARD_COUNT != 0:
        Guess = int(
            input(f"\nYou have {HARD_COUNT} attempts left .\nGuess the number : "))
        if Guess == guess_number:
            print(
                f"You guessed the number correct , it was {guess_number} !!! ")
            HARD_COUNT = 0
        elif Guess != guess_number and HARD_COUNT != 1:
            if Guess > guess_number:
                print("Too high , try again .")
                HARD_COUNT -= 1
            elif Guess < guess_number:
                print("Too low, try again .")
                HARD_COUNT -= 1
        elif Guess != guess_number and HARD_COUNT == 1:
            print(f"You lost , the number to guess was {guess_number} .")


if d_level == "easy":
    easy()
elif d_level == "hard":
    hard()
