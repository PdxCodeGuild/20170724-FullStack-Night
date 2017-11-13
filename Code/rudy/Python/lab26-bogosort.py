# Lab 26    Bogosort

import random


def is_sorted(shuffled_list):
    for num in range(len(shuffled_list)-1):
        if shuffled_list[num] > shuffled_list[num+1]:
            return False

    return True


def shuffler(nums):
    shuffled_list = []
    for i in range(len(nums)):
        random_index = random.randint(0, len(nums)-1)
        while nums[random_index] in shuffled_list:
            random_index = random.randint(0, len(nums)-1)
        num = nums[random_index]
        shuffled_list.append(num)
    return shuffled_list


def random_list():
    n = int(input('How many numbers would you like to sort? '))
    i = 0
    nums = []
    while i < n:
        num = random.randint(0,100)
        while num in nums:
            num = random.randint(0,100)
        nums.append(num)
        i += 1
    return nums


def main():
    nums = random_list()
    shuffled_list = shuffler(nums)
    print(is_sorted(shuffled_list))
    times_shuffled = 1
    while True:

        if is_sorted(shuffled_list) is False:
            shuffled_list= shuffler(shuffled_list)
            times_shuffled +=1
            print(is_sorted(shuffled_list))
            if is_sorted(shuffled_list) is True:
                break
    print(f'Shuffled {times_shuffled} times until sorted!')


main()
