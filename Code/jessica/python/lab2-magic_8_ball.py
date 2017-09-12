output = 'Welcome!'
print(output) #prints Welcome

question = input('Ask the 8-ball a question: ')#prints question and requires input


import random

predictions = ['Yes', 'It is decidedly so', 'No way!', 'All signs point to yes', 'Outlook not so good']
prediction = random.choice(predictions)
print(prediction)
