# generates and returns a list of length n, with random values between 0 and 100
import random


def random_list(n):
    random_list = []
    for i in range(n):
        random_list.append(random.choice(range(100)))
    return random_list

# randomly re-arranges a list
def shuffle(nums):
    # iterate through the indices of the list
    for i in range(len(nums)):
        # for each index, generate a random index
        j = random.randint(0, len(nums) - 1)
        # swap the elements at two indices
        nums[i], nums[j] = nums[j], nums[i]


# checks if a list is sorted
def is_sorted(nums):
    # iterate through the indices of the list
    false_count = 0
    for i in range(len(nums)-1):
        # if element at the current index is greater than the element at the next index: not sorted
        if nums[i] > nums[i+1]:
            return False
    # if you get through the entire list and each element is less than or equal to the next element: sorted
    return True


# continues to generate random arrangements until the list is sorted
def bogosort(nums):
    count = 0
    while not is_sorted(nums):
        shuffle(nums)
        print(nums)
        count += 1
    print(count)


nums = random_list(7)
print(nums)
bogosort(nums)
print(nums)

