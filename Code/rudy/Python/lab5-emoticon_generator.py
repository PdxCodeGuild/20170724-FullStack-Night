# Lab 5 Emoticon Generator

import random

eyes = ['^   ^', '*   *', '-   -', 'O   O']
noses = ['  o  ', '  0  ', '  v  ']
mouths = [' -U- ', ' >-< ', ' d-b ']

i = 0
while i < 10:
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    i = i + 1

    print(' -WWMWW-')
    print(' /' + eye + '\\ ')
    print('{ ' + nose + ' }')
    print(' |' + mouth + '| \n')

