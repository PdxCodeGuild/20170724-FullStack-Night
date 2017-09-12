# 2 write a function using random.randint and subscription to get a random element of a list and return it
import random


def choose_colors():
    colors = ['red', 'orange', 'green', 'blue', 'yellow']
    number = random.randint(0, len(colors) - 1)  # random.randint chooses number between and including the numbers
    return colors[number]
print(choose_colors())