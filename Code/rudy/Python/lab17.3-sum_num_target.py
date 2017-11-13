#   Lab 17.3 Pair of Numbers in List equal to Sum


import random


def randomized_list():
    random_list = []
    for i in range(20):
        num = random.randint(1,10)
        random_list.append(num)
    return random_list


def sum_nums(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                    print(i, j)


def main():
    target = int(input('Enter a number under 20: '))
    while 2 > target < 20:
        if 2 > target < 20:
            print('error')

    nums = randomized_list()
    print(nums)

    target_pair = sum_nums(nums, target)
    #print(target_pair)

main()
