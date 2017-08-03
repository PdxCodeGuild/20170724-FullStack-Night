import random



word = ['cat', 'dog', 'elephant', 'bear', 'rabbit', 'hippo']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']



i = 0

while i < 5:
    word_2 = random.choice(word)
    num_2 = random.choice(num)
    password = word_2 + num_2

    print(password)
    i += 1