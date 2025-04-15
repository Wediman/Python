import random
from art import g_game

print(g_game)

def high_low(guess, number_to_guess):
    if guess > number_to_guess:
        print("Too High")
    elif guess < number_to_guess:
        print("Too Low")

def easy():
    l_game = 10
    number_to_guess = random.randint(1, 100)
    print(number_to_guess)
    while l_game != 0:
        print(f"You have {l_game} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You guessed right! The answer was {number_to_guess}")
            exit()
        elif guess != number_to_guess:
            high_low(guess, number_to_guess)
            print("Guess again.")
            l_game -= 1
    if l_game == 0:
        print("You've run out of guesses, you lose.")

def hard():
    l_game = 5
    number_to_guess = random.randint(1, 100)
    print(number_to_guess)
    while l_game != 0:
        print(f"You have {l_game} attemps remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You guessed right! The answer was {number_to_guess}")
            exit()
        elif guess != number_to_guess:
            high_low(guess, number_to_guess)
            print("Guess again.")
            l_game -= 1
    if l_game == 0:
        print("You've run out of guesses, you lose.")

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number bewteen 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        easy()
    elif difficulty == "hard":
        hard()

game()