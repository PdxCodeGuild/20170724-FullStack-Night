import random

eyes = [':', ';']
noses = ['-', '>']
mouths = [')', '(']

generator_eyes = random.choice(eyes)
generator_noses = random.choice(noses)
generator_mouths = random.choice(mouths)
emoticon_generator = generator_eyes + generator_noses + generator_mouths


print(emoticon_generator)

