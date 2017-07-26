welcome = input('Welcome to the Magic 8 Ball. press "ENTER"')
start = input('Type your question here --> ')
print(welcome)


question = start
print(question + ' That\'s a good question. Let\'s ask the Magic 8 Ball')

shake = input('  {   {  { {shaking} }  }  }  ')
print(shake)

import random
answers = ['It is certain', 'It is decidedly so', 'Without a doubt','Yes, definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later']
answer = random.choice(answers)
print(answer)



# import random
# nums = [5, 7, 8]
# num = random.choice(nums)
# print(num)

# fruits = ['apples', 'bananas', 'pears']
# fruit = random.choice(fruits)
# print(fruit)


