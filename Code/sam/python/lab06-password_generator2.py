import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

user_input = input('How many characters do you want in your password? ')
user_input = int(user_input)

password = ''

i = 0
while i < user_input:
    password = password + random.choice(alphabet)
    i += 1

print(password)



