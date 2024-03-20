import random

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

#Write your code below this line 👇

oponent_choices = random.choice([rock, paper, scissors])
print(oponent_choices)
player_choice = input("Your choice in rock, paper or scissors is ?")

if player_choice.lower() == "rock":
    player_choice = rock
elif player_choice.lower() == "paper":
    player_choice = paper
elif player_choice.lower() == "scissors":
    player_choice = scissors
else:
    print("Invalid message")
    exit(-1)

if player_choice == oponent_choices:
    print("your choice is \n" + player_choice)
    print("opponent choice is \n" + oponent_choices)
    print("It's a handed over")
elif (oponent_choices == rock and player_choice == scissors) or oponent_choices == scissors and player_choice == paper or oponent_choices == paper and player_choice == rock:
    print("your choice is \n" + player_choice)
    print("opponent choice is \n" + oponent_choices)
    print("you loose")
else:
    print("your choice is \n" + player_choice)
    print("opponent choice is \n" + oponent_choices)
    print("you win")

