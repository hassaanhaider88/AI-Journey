import random

randomNumber = random.randint(1, 10)
tries = 0
while True:
    userNum = int(input("Enter your guess: "))
    tries += 1
    if userNum == randomNumber:
        print("You guessed the number correctly!")
        print(f"You got it in {tries} tries.")
        break
    elif userNum < randomNumber:
        print("Your guess is too low. Try again!")
    else:
        print("Your guess is too high. Try again!")