import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_list = [rock, paper, scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print("your choice:-")
print(game_list[your_choice])
random_choice = random.randint(0, 2)
print(f"Computer chose:-{random_choice}")
print(game_list[random_choice])
if your_choice == 0 and random_choice == 2:
    print("You Win!")
elif your_choice == 2 and random_choice == 1:
    print("You Win!")
elif your_choice == 1 and random_choice == 0:
    print("You Win!")
elif random_choice == 0 and your_choice == 2:
    print("You lose")
elif random_choice == 2 and your_choice == 1:
    print("You lose!")
elif random_choice == 1 and your_choice == 0:
    print("You lose!")
elif your_choice == random_choice:
    print("It's a Draw")
