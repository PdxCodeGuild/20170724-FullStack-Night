# Lab 4: Rock Paper Scissors

import random  # import will provide a function outside of this source code

# r = rock
# p = paper
# s = scissors
playing = True

while playing:

    #print('Rock = r')
    #print('Paper = p')
    #print('Scissor = s')
    player1 = input('Player 1, please choose a weapon -> ')

    r = 'r'
    p = 'p'
    s = 's'

    weapons = ['r', 'p', 's']
    weapon = random.choice(weapons)
    print('Computer chooses ' + weapon)

    computer = weapon

    if player1 == computer :
        print('It\'s a TIE. Try again?')

    elif player1 == r and computer == p:
        print('You LOSE! Play Again?')

    elif player1 == r and computer == s:
        print('You WIN! Play Again?')

    elif player1 == p and computer == r:
        print('You WIN! Play Again?')

    elif player1 == p and computer == s:
        print('You LOSE! Play Again?')

    elif player1 == s and computer == r:
        print('You LOSE! Play Again?')

    elif player1 == s and computer == p:
        print('You WIN! Play Again?')

    else:
        print('Computer went Nuclear, get to your bunker NOW!!!')
        break
