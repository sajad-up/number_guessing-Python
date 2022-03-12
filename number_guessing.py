import random

# range of random numbers between 1-10
n = random.randrange(1, 10)

# user input
guess = int(input("Guess the Number between 1 to 10: "))

while n != guess:
    # if guess is smaller than n
    if guess < n:
        print("Your guess is smaller than actual number")
        guess = int(input("Enter again: "))

    # if guess is greater than n
    elif guess > n:
        print("Your guess is greater than actual number")
        guess = int(input("Enter again: "))

    else:
        break

print("you win!")
