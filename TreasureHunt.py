print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a cross road.Where do you want to go?")
direction = input('         Type "left" or "right".\n').lower()

if direction == "left":
    print("You have come to a lake.There is an island in the middle of the lake.")
    move = input('Type "wait" to wait for a boat.Type "swim" to swim across.\n').lower()
    if move == "wait":
        print("You arrive at the island unharmed.There is a house with three doors.")
        doors = input("One red,One yellow and One blue.Which one do you choose?\n").lower()
        if doors == "yellow":
            print("Hooray!You have found the treasure!")
        elif doors == "red":
            print("There is a raging fire behind the door, hence the colour of the door.Game Over")
        elif doors == "blue":
            print("The room behind the door is filled with water.Game Over")
    elif move == "swim":
        print("Sadly you drowned")
elif direction == "right":
        print("You went the wrong way and there is nothing there.Game Over")
else:
    print("Wrong Input.")
