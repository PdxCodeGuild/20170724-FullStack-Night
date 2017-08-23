# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
def combine_all(nums):
    all_nums = []
    for num in nums:
        for num1 in num:
            all_nums.append(num1)
    print(all_nums)
combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]])
