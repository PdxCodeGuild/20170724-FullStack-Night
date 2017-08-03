# Practice 3    Returning Function

    #def maximum_of_three(a, b, c)
    #maximum_of three(5, 6, 2) will return 6
    #maximum_of_three(-4, 3, 10) will return 10

import random


def maximum_of_three(a, b, c):  # compare a to b; a to c; b to c. assign a value for each and return the higher of the 3
    if a > b:
        if a > c:
            print(str(a) + str(' is the maximum of the three numbers!'))
        else:
            print(str(c) + str(' is the maximum of the three numbers!'))
    else:
        if b > c:
            print(str(b) + str(' is the maximum of the three numbers!'))
        else:
            print(str(c) + str(' is the maximum of the three numbers!'))


def random_number_gen():
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    return a, b, c


def main():
    a, b, c = random_number_gen()
    print(a, b, c)

    maximum_of_three(a, b, c)


main()

