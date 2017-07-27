
print('Lets PLAY Rock, Paper, Scissors!')
print('\v') #space
player = input ('Rock(R), Paper(P), Scissors(S)?:')

import random

computer = ['R', 'P', 'S']
computer = random.choice(computer)
print (computer)


if player == computer:
    print('TIE!!')
elif player == 'R' and computer == 'P':
    print('Computer Wins!')
elif player == 'R' and computer == 'S':
    print('You Wins!')
elif player == 'P' and computer == 'R':
    print('You Wins!')
elif player == 'P' and computer == 'S':
    print('Computer Win!')
elif player == 'S' and computer == 'R':
    print('Computer Wins!')
elif player == 'S' and computer == 'P':
    print('You Wins!')
else:
    print('Game Over')
