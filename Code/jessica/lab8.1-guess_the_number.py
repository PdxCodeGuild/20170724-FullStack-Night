import random


computer = random.randint(0, 10)



guess = 0
while guess < 10:
    x = int(input('Guess a number between 1 and 10: '))
    if x == computer:
        print('You guessed right!')
        break
    else:
        print('Guess again. ')
    guess += 1

if guess >= 10:
    print('You lose.')

guesses = 10
print('guesses: ' + str(guesses))








