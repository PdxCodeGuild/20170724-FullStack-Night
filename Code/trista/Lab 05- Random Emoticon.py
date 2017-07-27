print('Lets build a face:')

import random

eyes = [':', '=', ';']
eyes = random.choice(eyes)

noses = ['>', 'v', '<']
noses = random.choice(noses)

mouths = [')', '/', '(']
mouths = random.choice(mouths)


print(eyes + noses + mouths)


