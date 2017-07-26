import random

eyes = [':', ';']
noses = ['-', ' ']
mouths = [')', '(']

i = 0
while i < 5:
    generator_eyes = random.choice(eyes)
    generator_noses = random.choice(noses)
    generator_mouths = random.choice(mouths)
    emoticon_generator = generator_eyes + generator_noses + generator_mouths
    print(emoticon_generator)
    i += 1

