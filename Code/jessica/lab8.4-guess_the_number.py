from random import randint

computer_number = randint(1, 10)
# have computer pick random number

# Let user pick a number
guesses = 1
while guesses < 12:
    if guesses == 11:
        print('You lose!')
        guesses += 1
        continue
    else:
        guess = int(input('This is guess {}. Please guess a number between 1 and 10: '.format(guesses)))

    # Have computer tell the user if the guess is hi or low

    if abs(guess - computer_number) >= 3:
        print('You are cold!')
    elif abs(guess - computer_number) == 2:
        print('You are getting warmer!')
    elif abs(guess - computer_number) == 1:
        print('You are hot!')
    elif guess == computer_number:
        print('You win!')
        break
    guesses += 1
else:
    print('My number was {}'.format(computer_number))
# If a user pick the right number tell them they won.

# computer = 5
# human = 2
# print(abs(computer - human))