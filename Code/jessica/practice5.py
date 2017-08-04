# 5 write functions to find the minimum, maximum, mean, and mode of a list of numbers
def minimum(nums):
    min_value = nums[0]
    for num in nums:
        # if num is less than min-value
        if num < min_value:
            # then set min value to num
            min_value = num
    return min_value

def maximum(nums):
    max_value = nums[0]
    for num in nums:
        #if num is greater than max_value
        if num > max_value:
            #then set min value to num
            max_value = num
    return max_value

def mean(nums):
    total = 0
    list_len = len(nums)
    for n in nums:
        total += n
    mean = total / list_len
    return mean

#mode the most frequently occurring number
def mode(nums):

    return mode

def median(nums):
    #sort list and find middle number
    sortednums = list(sorted(nums))
    list_len = len(sortednums)
    index = list_len // 2
    return sortednums[index]

#alternate sort method
def median2(nums):
    sortednums2 = nums.copy()
    sortednums2.sort()
    list_len = len(sortednums2)
    index = list_len // 2
    return sortednums2[index]


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minimum(nums), maximum(nums), mean(nums), median(nums), median2(nums)
          )

main()

