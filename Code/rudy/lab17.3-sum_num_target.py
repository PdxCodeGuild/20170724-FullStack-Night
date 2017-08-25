#   Lab 17.3 Pair of Numbers in List equal to Sum


import random

def randomized_list():
    random_list = []
    for i in range(20):
        num = random.randint(1,10)
        random_list.append(num)
    return random_list


def sum_nums(target,random_list):
    for i in range(len(random_list)):



        return i

def main():
    target = int(input('Enter a number under 20: '))
    while 2 > target < 20:
        if 2 > target < 20:
            print('error')

    random_list = randomized_list()
    print(random_list)

    i = sum_nums(target, random_list)
    print(i)
main()
