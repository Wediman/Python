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

game_image = [rock, paper, scissors]

player_1 = int(input('Type "0" for Rock, "1" for Paper, and "2" for Scissors : '))
if player_1 >= 3 or player_1 < 0:
    print("Invalid")
else:
    print(game_image[player_1])

    enemy = random.randint(0, 2)
    print(game_image[enemy])

    if player_1 == 0 and enemy == 2:
        print("You Win!")
    elif player_1 == 2 and enemy == 0:
        print("You Lose")
    elif enemy > player_1:
        print("You Lose!")
    elif player_1 > enemy:
        print("You Win")
    elif enemy == player_1:
        print("Its a Draw!")
