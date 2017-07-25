print ('Welcome to Lab02')
print('\v')  #space between lines
question = input ('Ask the Magic 8-Ball anything:') #user will ask a random question

import random

answers = ['Yes!', 'Not really', 'I think not', 'Absolutely', 'Maybe so'] #python will choose an answer from the brackets
answer = random.choice(answers)
print(answer)
