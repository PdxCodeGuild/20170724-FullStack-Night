# Lab 8.2 Guess the Number - infinite tries.

import random


computer = random.randint(1, 100)  # variable computer is being assigned a number between 1 and 10 using the random module's function of random integer.
print(computer)

attempt = 0
while True:
    guess = input('Guess a number between 1 and 100 -> ')
    guess = int(guess)
    if guess > 100 or guess < 1:
        print('Sorry, please choose a number between 1 and 100 ->')
        continue
    elif guess == computer:
        print('Congratulations! The computer did choose ' + str(guess))
        break
    print('Attempt ' + str(attempt +1) + ': ' + 'You guessed ' + str(guess))
    attempt = attempt + 1