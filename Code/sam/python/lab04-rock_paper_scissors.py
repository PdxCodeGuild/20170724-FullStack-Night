import random

rps = ['rock', 'paper', 'scissors']
comp_choice = random.choice(rps)

user_choice = input('Rock, paper or scissors? ')

print('Computer chose:' + comp_choice)
print('You chose:' + user_choice)

if comp_choice == user_choice:
    print('Tie!')
elif comp_choice == 'rock' and user_choice == 'paper':
    print('You win!')
elif comp_choice == 'rock' and user_choice == 'scissors':
    print('Computer wins!')
elif comp_choice == 'scissors' and user_choice == 'paper':
    print('Computer wins!')
elif comp_choice == 'scissors' and user_choice == 'rock':
    print('You win!')
elif comp_choice == 'paper' and user_choice == 'rock':
    print('Computer wins!')
elif comp_choice == 'paper' and user_choice == 'scissors':
    print('You win!')

