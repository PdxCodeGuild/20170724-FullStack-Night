import random

eyes = ('=', ':', ';')
nose = ('>', ')')
mouth = ('D', 'P', '|', ')', '(')


i = 0
while i < 5:
    eyes_2 = random.choice(eyes)
    nose_2 = random.choice(nose)
    mouth_2 = random.choice(mouth)
    emoticon = eyes_2 + nose_2 + mouth_2
    print(emoticon)
    i += 1

