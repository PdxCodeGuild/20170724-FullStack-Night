# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

nums = [5, 6, 2, 3]
target_number = 7


# compare each element of the list to other elements of the list
def find_pair(nums, target_number):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target_number:
                print(f' {nums[i]} {nums[j]}')
find_pair(nums, target_number)



