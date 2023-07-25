

#007
#treasure island


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treaasure island . \nYour mission is to find the treasure  .")
road=input("There are two roads forward , choose one (Left or Right)")
if road=="left" or road=="Left" or road=="LEFT" or road=="L" or road=="l":
    print("oops , you reached a dead end ...")
elif road=="right" or road=="Right" or road=="RIGHT" or road=="R" or road=="r":
    water=input("you have reached a river , would you like to wait(w) or swim(s)")
    if water=="wait" or water=="w" :
        print ("Game over , you died of hunger .")
    elif water=="swim" or water=="s":
        doors=input("You crossed the river and now reached three doors blue(b) , red(r) , green(g) , choose one ")
        if doors=="red" or doors=="r":
            print("You win , Enjoy the Treasure !!!!!!")
        elif doors=="green" or doors=="g":
            print("oops , you walked into the poisenous gas !!!!")
        else :
            print("Damn You just walked into a room full of karens , sorry mate we feel for u 😢")

