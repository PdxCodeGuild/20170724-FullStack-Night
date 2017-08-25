# Practice 2    Random Integer & Subscription

import random


def random_int_gen(a_list):

    a = random.randint(0, len(a_list) - 1)  # the variable a
    print(a_list[a])


def main():
        a_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        random_int_gen(a_list)


main()



