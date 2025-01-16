#24
import random
# Guess the number game
number = random.randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")