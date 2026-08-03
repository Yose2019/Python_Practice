import random

def guessNumber():
    randomGenerate = random.randint(0,20)

    while True:
        guess = int(input("Enter a number between 1 to 20 (inclusive):"))
        if guess >= 0 and guess<=20:
            if guess == randomGenerate:
                print("The guess is right")
                break
            else:
                print("Oops not quite right, try again")
                continue
        else:
            print("Guess a number between 1 and 20")


guessNumber()
            

