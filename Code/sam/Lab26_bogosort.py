import random

# generates and returns a list of length n, with random values between 0 and 100


def random_list(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,100))
    return list


# randomly re-arranges a list

nums = random_list(10)
print(nums)

def shuffle(nums):
    for i in range(len(nums)):
        j = random.randint(0, len(nums)-1)
        nums[i], nums[j] = nums[j], nums[i]


shuffle(nums)
print(nums)

# checks if a list is sorted

def is_sorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):
    count = 0
    while not is_sorted(nums):
        if is_sorted(nums):
            return nums
        shuffle(nums)
        count += 1
        print(nums)
    print(count)

print(bogosort(nums))







