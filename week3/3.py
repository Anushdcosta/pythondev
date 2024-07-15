import random

answer = random.randrange(0, 100)

while True:
    guess = int(input("Enter your guess a number between 1 to 100: "))
    if guess == answer:
        print("Congratulations! You guessed it!")
        break
    elif guess > answer:
        print("Too high!")
    elif guess < answer:
        print("Too low!")

    