
import random


x = input('Choose: rock, paper, scissors ')

computer_chooses = ['rock', 'paper', 'scissors']
computer = random.choice(computer_chooses)
print(computer)

if x == 'rock' and computer == 'rock':
    print('Tie')
elif x == 'rock' and computer == 'paper':
    print('Computer wins')
elif x == 'rock' and computer == 'scissors':
    print('You win')
elif x == 'paper' and computer == 'rock':
    print('You win')
elif x == 'paper' and computer == 'paper':
    print('Tie')
elif x == 'paper' and computer == 'scissors':
    print('Computer wins')
elif x == 'scissors' and computer == 'rock':
    print('Computer wins')
elif x == 'scissors' and computer == 'paper':
    print('You win')
elif x == 'scissors' and computer == 'scissors':
    print('Tie')
else:
    print('Game over')


