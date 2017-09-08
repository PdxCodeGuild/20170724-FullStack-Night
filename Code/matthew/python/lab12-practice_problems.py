"""
lab 12: practice problems
"""

import random

# problem 1: even or odd --------------------


def is_even(a):
    # return a/2 == a//2
    return a%2 == 0


def is_odd(a):
    # return a/2 != a//2
    return a%2 == 1

# problem 2: random element using randint --------------------


def random_element(a):
    index = random.randint(0, len(a)-1)
    return a[index]

# problem 3: maximum of three values --------------------


def maximum_of_two(a, b):
    if a > b:
        return a
    return b


def maximum_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


# problem 4: print the powers of 2 --------------------


def print_powers_of_two(n):
    for i in range(n):
        print(2 ** i)

# problem 5: min, max, mean, median, mode --------------------


def minimum(nums):
    if len(nums) == 0:
        return None
    min_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
    return min_value


def minimum2(nums):
    min_value = None
    for num in nums:
        if min_value is None or num < min_value:
            min_value = num
    return min_value


def maxmimum(nums):
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
    return max_value


def median(nums):  # assume nums is sorted
    # nums.sort()
    if is_odd(len(nums)):
        index = len(nums)//2
        return nums[index]
    else:
        index = len(nums)//2
        return [nums[index], nums[index+1]]


def mean(nums):
    total = 0
    for num in nums:
        total += num
    return total/len(nums)


def mode(nums):
    counts = [0]*len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] == nums[j]:
                counts[i] += 1
    print(counts)
    max_count = max(counts)
    mode_index = counts.index(max_count)
    return nums[mode_index]


# print(mode([5, 5, 6, 7, 7, 7, 8]))


# problem 6: reverse a list --------------------

# alternative ways to reverse
# x = [5, 6, 7, 8]
# x.reverse()
# print(list(reversed(x)))
# print(x[::-1])


def reverse(nums):
    rev_nums = []
    for num in nums:
        rev_nums.insert(0, num)
    return rev_nums


def reverse_v2(nums):
    for i in range(len(nums) // 2):
        j = len(nums) - i - 1
        # print(str(i) + ' ' + str(j))

        # swap the elements at i and j
        # t = nums[i]
        # nums[i] = nums[j]
        # nums[j] = t

        # a more python way to swap
        nums[i], nums[j] = nums[j], nums[i]


# nums = [5, 6, 7, 8, 9, 10, 11, 12]
# reverse(nums)
# print(nums)

# problem 7: common elements between two lists --------------------


def common_elements(list1, list2):
    list3 = []
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                list3.append(elem1)
    return list3

# problem 8: add numbers less than 10 to a new list --------------------


def extract_less_than_ten(nums):
    list3 = []
    for num in nums:
        if num < 10:
            list3.append(num)
    return list3


# problem 9: combine two lists, alternating elements --------------------


def combine(list1, list2):
    list3 = []
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3


# v2 - combine two lists, alternating elements, adding any extras on the end
def combine_v2(list1, list2):

    if len(list1) > len(list2):
        list1, list2 = list2, list1  # swap, so the smaller is first

    list3 = []
    i = 0
    while i < len(list1):
        list3.append(list1[i])
        list3.append(list2[i])
        i += 1

    while i < len(list2):
        list3.append(list2[i])
        i += 1

    return list3


# print(combine(['a','b','c'],[1,2,3]))
