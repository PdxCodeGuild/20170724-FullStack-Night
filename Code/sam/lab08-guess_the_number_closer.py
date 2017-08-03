import random

number = random.randint(1, 10)

last_guess = None


while True:
    user_guess = int(input('Pick a number between 1 and 10. '))
    if number == user_guess:
        print('Correct!')
        break
    if last_guess is not None:
        d_guess = abs(number - user_guess)
        d_last_guess = abs(target - last_guess)
        if d_guess < d_last_guess:
            print('closer')
        else:
            print('further')

    print('guess: ' + str(guess))
    print('last guess:' + str(last_guess))




