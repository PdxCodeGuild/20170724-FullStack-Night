nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         # list of nums
target = 3                                        # target sum


def find_pairs(nums,target):
    pairs = []                                    # empty list of pairs
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i + j == target:                   # checking if i + j is equal to target
                pairs.append([nums[i], nums[j]])  # if equal append to pairs in list
    return pairs

print(find_pairs(nums,target))
