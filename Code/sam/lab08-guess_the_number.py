import random
number = random.randint(1, 10)


i = 0
while i < 10:
    user_guess = int(input('Pick a number between 1 and 10. '))
    if number == user_guess:
        print('Correct!')
        break
    if number < user_guess:
        print('Lower')
    if number > user_guess:
        print('Higher')

    i += 1