# Lab 8.4 Guess the Number

import random

computer = random.randint(1,
                          10)  # variable computer is being assigned a number between 1 and 10 using the random module's function of random integer.
print(computer)

attempt = 0
while True:
    guess = input('Guess a number between 1 and 10 -> ')
    guess = int(guess)
    if guess > 10 or guess < 1:
        print('Sorry, please choose a number between 1 and 10 ->')
        continue

    elif guess == computer:
        print('Congratulations! The computer did choose ' + str(guess))
        break
    elif guess > computer:
        print('Your guess is too high!')
    elif guess < computer:
        print('Your guess is too low!')

    print('Attempt ' + str(attempt + 1) + ': ' + 'You guessed ' + str(guess))
    attempt = attempt + 1
