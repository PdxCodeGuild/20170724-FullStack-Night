print('Lets build a face:')

import random

eyes = [':', '=', ';']
eyes = random.choice(eyes)

noses = ['>', 'v', '<']
noses = random.choice(noses)

mouths = [')', '/', '(']
mouths = random.choice(mouths)

emotions = ['Happy', 'Mad', 'Sad', 'Silly', 'Flirty']
emotions = random.choice(emotions)

print(eyes + noses + mouths + emotions)


