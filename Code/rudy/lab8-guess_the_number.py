# Lab 8 Guess the Number

# First we need to build a random number generator for the computer with parameters of choosing a number between 1 and 10. Then store that number as an integer.

# Second, build an input function to have the user guess a number. Optional: build rules that the user cannot guess a number outside the given parameters of 10 or they will need to guess again.

# If the user guess is not equal to the computer number, then have them try again using a while loop to give them 10 tries.

import random


computer = random.randint(1, 10)  # variable computer is being assigned a number between 1 and 10 using the random module's function of random integer.
print(computer)

attempt = 0
while attempt < 10:
    guess = input('Guess a number between 1 and 10 -> ')
    guess = int(guess)
    if guess > 10 or guess < 1:
        print('Sorry, please choose a number between 1 and 10 ->')
        continue
    elif guess == computer:
        print('Congratulations! The computer did choose ' + str(guess))
        break
    print('Attempt ' + str(attempt +1) + ': ' + 'You guessed ' + str(guess))
    attempt = attempt + 1
