from numbers import Number

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice_list = [rock, paper, scissors]
user = int(input("What do you choose?Type 0 for Rock, type 1 for Paper or 2 for scissors.\n"))
opponent_index = (random.randint(0,2))

print("Player chose:")
print(choice_list[user])
print("Opponent chose:")
print(choice_list[opponent_index])


if user == 0 and opponent_index == 0:
    print("It`s A Draw!")
elif user == 0 and opponent_index == 2:
    print("User Wins!")
elif user == 1 and opponent_index == 0:
    print("User Wins!")
elif user == 2 and opponent_index == 1:
    print("Player Wins!")
else:
    print("Opponent Wins!")
