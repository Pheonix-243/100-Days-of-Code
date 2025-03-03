# ===================================
# TREASURE ISLAND GAME 🏝️
# ===================================
# A simple adventure game using if-else statements with ASCII art.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_."  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.-"o.-"_/______/______/______/
____/______/______/______/______/____"=.o|o_.--""____/______/______/______/
*******************************************************************************
''')
print("🏝️ Welcome to Treasure Island! 🏝️")
print("Your mission is to find the treasure. 🏆\n")

# First decision
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    print('''
       ~  ~
   ~         ~
     ~   🚣   ~
  ~        ~
    ~  ~
    ''')

    # Second decision
    choice2 = input("You've come to a lake. Do you wait for a boat or swim across? Type 'wait' or 'swim': ").lower()

    if choice2 == "wait":
        print('''
        ⛵  You waited and a boat arrived! Now you sail to an island. ⛵
        ''')

        # Third decision
        choice3 = input(
            "You arrive at a house with three doors: red, blue, and yellow. Which one do you choose? ").lower()

        if choice3 == "yellow":
            print('''
            🏆 YOU FOUND THE TREASURE!!! 🎉
            🎁 💰 💎
            ''')
        elif choice3 == "red":
            print('''
            🔥 The room was filled with fire. You got burned! Game Over. 🔥
            ''')
        elif choice3 == "blue":
            print('''
            🦈 A wild beast attacked you! Game Over. 🦈
            ''')
        else:
            print('''
            🚪 That door doesn’t exist. Game Over.
            ''')

    else:
        print('''
        🌊 A giant sea monster attacked you! Game Over. 🌊
        ''')

else:
    print('''
    💀 You fell into a hole. Game Over. 💀
    ''')
