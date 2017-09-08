import random
user_choice = int(input('Choose a number between 1 and 10. '))

# create a list of previous guesses
previous_guesses = []

i = 0
while i < 10:
    while True:
        comp_guess = random.randint(1, 10)
        # if comp_guess not in previous guesses, continue guessing.
        if comp_guess not in previous_guesses:
            break
    # add comp_guess to previous guess list
    previous_guesses.append(comp_guess)

    if comp_guess == user_choice:
        print('The computer guessed: ' + str(comp_guess))
        print('Computer wins!')
        break
    if comp_guess > user_choice:
        print('The computer guessed: ' + str(comp_guess))
    if comp_guess < user_choice:
        print('The computer guessed: ' + str(comp_guess))

    i += 1


