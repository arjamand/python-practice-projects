# 2022-11-01 17:25:32

# import clear
# Clearing the Screen

# import os
import random
import clear

from art import logo
from art import vs
from game_data import data
score = 0
compare_a = random.choice(data)
against_b = random.choice(data)
# print(logo)
# print(logo)
score__ = (f"Your current score is {score} .")
# option=(input("Who has more followers (A or B): ")).lower()


def compare():
    """Main comparing program"""
    # start()
    print(logo)

    print(score__)
    global against_b
    global compare_a
    signal = True
    while signal is True:
        if compare_a['name'] == against_b['name']:
            compare_a = random.choice(data)
        elif compare_a['name'] != against_b['name']:
            signal = False
    followers_b = against_b['follower_count']
    followers_a = compare_a['follower_count']

    def compareA():
        """Simple print Function for a specific 
        """
        print(
            f"Compare A : {compare_a['name']} , {compare_a['description']} , {compare_a['country']} . ")

    def againstB():
        """simple print function
        """
        print(
            f"Against B : {against_b['name']} , {against_b['description']} , {against_b['country']} . ")
    compareA()
    print(vs)
    againstB()
    selection = (input("\nWho has more followers (A or B): ")).lower()
    global score
    if selection == "a":
        if followers_a > followers_b:
            # global score
            score += 1
            against_b = random.choice(data)
            clear.clear()
            # start()
            compare()
        elif followers_a < followers_b:
            print(
                f'Sorry that\'s wrong , you lost !!! \n\nYour score is : {score} \n')
    elif selection == "b":
        if followers_a > followers_b:
            print(
                f'Sorry that\'s wrong , you lost !!! \n\nYour score is : {score} \n')
        elif followers_b > followers_a:
            # global score
            score += 1
            compare_a = against_b
            against_b = random.choice(data)
            # start()a
            clear.clear()
            compare()


compare()
# print(compare_a)
