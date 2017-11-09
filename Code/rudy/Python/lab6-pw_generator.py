# Lab 6 Password Generator

import random

n = input('How many characters do you want your password to have? ')

n = int(n)

password = ''
i = 0
while i < n:
    characters = '12345aeiouRSTLN@#$%&'
    character = random.choice(characters)
    password += character           # password = password + character
    i = i + 1                       # add i until it reaches n
print(password)                     # <---pushing outside of loop gives you final result


