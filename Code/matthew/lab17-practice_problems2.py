

def collect_numbers():
    nums = []
    while True:
        num = input('enter a number (or \'done\'): ')
        if num == 'done':
            break
        else:
            nums.append(int(num))
    print(nums)


def print_every_other_while(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 2


def print_every_other_for(nums):
    for i in range(0, len(nums), 2):
        print(nums[i])


def find_pairs(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append([nums[i], nums[j]])
    return pairs


def double_letters(text):
    r = ''
    for char in text:
        r += char + char
    return r


def merge(list1, list2):
    r = []
    for i in range(len(list1)):
        r.append([list1[i], list2[i]])
    return r