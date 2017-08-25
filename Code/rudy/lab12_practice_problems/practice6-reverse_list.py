#   Practice 6  Reverse List

import random


def random_list():
    n = random.randint(10, 30)
    r = []
    for i in range(n):
        r.append(random.randint(0, 100))
    return r


def reverse_list(nums):
    rev_nums = []
    for num in nums:
        #  print(rev_nums)
        rev_nums.insert(0, num)
    return rev_nums


def main():
    r = random_list()
    print(r)

    rev_nums = reverse_list(r)
    print(rev_nums)


main()

