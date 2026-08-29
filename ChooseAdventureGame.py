#This is a Treasure Island 'choose your own adventure' game
#ASCII art is obtained from https://ascii.co.uk/art

print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

print("Welcome to Treasure Island!\n")
print("Your mission is to find the treasure.\n")
print("You arrive at a crossroad. Which way would you like to go? Left or right?\n")
choice = input()
if choice == "left":
    print("Now you've come to a lake with an island in the middle. Will you swim or wait?\n")
    choice = input()
    if choice == "wait":
        print("You arrive at a castle on the island with three doors, one red, one blue, one yellow. Which do you choose? Or do you choose none?\n")
        choice = input()
        if choice == "red":
            print("You just got burned by fire. Game over.\n")
        elif choice == "blue":
            print("You just got eaten by beasts. Game over.\n")
        elif choice == "yellow":
            print("Congratulations! You win! A gleaming treasure chest awaits you!\n")
        else:
            print("Game over.")
    else:
        print("You are attacked by trout. Game over.")
else:
    print("You fall into a hole. Game over.")
