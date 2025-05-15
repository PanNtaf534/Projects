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
player = int(input("What do you choose?Type 0 for Rock, type 1 for Paper or 2 for scissors.\n"))
if player not in [0, 1, 2]: exit("Invalid input. Please enter 0, 1, or 2.")
opponent_index = (random.randint(0,2))

print("Player chose:")
print(choice_list[player])
print("Opponent chose:")
print(choice_list[opponent_index])


if player == 0 and opponent_index == 0:
    print("It`s A Draw!")
elif player == 0 and opponent_index == 2:
    print("Player Wins!")
elif player == 1 and opponent_index == 0:
    print("Player Wins!")
elif player == 2 and opponent_index == 1:
    print("Player Wins!")
else:
    print("Opponent Wins!")
