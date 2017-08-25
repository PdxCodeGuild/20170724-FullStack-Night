#   Practice 4  Min Max Mean Mode


import random


def random_list():
    n = random.randint(10, 30)
    r = []
    for i in range(n):
        r.append(random.randint(0, 100))
    return r


def minimum(nums):
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value


def maximum(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value


def mean(nums):
    total_nums = len(nums)
    total_sum = 0
    i = 0
    while i < total_nums:
        total_sum += nums[i]
        i += 1

    mean_value = total_sum / total_nums
    return mean_value


def mode(nums):
    counts = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                counts[i] += 1
    print(counts)
    max_count = max(counts)
    mode_index = counts.index(max_count)
    return nums[mode_index]

'''
    total_nums = len(nums)
    i = 0
    num_count = 1
    for num in nums:
        if num[i] == num[i + 1]:
            num_count = num[i] + 1
        for num
'''

def main():
    r = random_list()
    print(r)

    min_value = minimum(r)
    print('Minimum number in the list is ' + str(min_value))

    max_value = maximum(r)
    print('Maximum number in the list is ' + str(max_value))

    mean_value = mean(r)
    print('Mean number in the list is ' + str(mean_value))

    mode_value = mode(r)
    print('Mode number that occurs the most in this list is ' + str(mode_value))


main()
