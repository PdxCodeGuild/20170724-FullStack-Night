import random


computer = random.randint(0, 10)



guess = 0
while True:
    x = int(input('Guess a number between 1 and 10: '))
    if x == computer:
        print('You guessed right!')
        break
    elif x > computer:
        print('You guessed too high!')
    elif x < computer:
        print('You guessed too low!')
    else:
        print('Guess again. ')
    guess += 1



print('guesses: ' + str(guess))