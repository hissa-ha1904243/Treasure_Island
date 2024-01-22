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

print("Welcome to treasure island!")
print("Your mission is to find the treasure")

ans1 = input('You\'re at a crossroad. Where do you want to go? Write "left" or "right". \n')


if ans1.lower() == "right":
    print("Game Over!")
elif ans1.lower() == "left":
    ans2 = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. "
                 "Type \"swim\" to swim across. \n")
    if ans2.lower() == "swim":
        print("Game Over!")
    elif ans2.lower() == "wait":
        ans3 = input("You arrived at the island unharmed. There is a house with 3 doors."
                     " One red, one yellow, and one blue. Which color do you choose?\n")
        if ans3.lower() == "red":
            print("Game Over!")
        elif ans3.lower() == "yellow":
            print("YOU WIN!")
        elif ans3.lower() == "blue":
            print("Game Over!")
        else:
            print("invalid input!")
    else:
        print("invalid input!")
else:
    print("invalid input!")
