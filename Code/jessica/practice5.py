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
    sorted_list = nums.sort()
    list_len = len(nums)
    index = list_len // 2
    return nums[index]

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(minimum(nums), maximum(nums), mean(nums), median(nums))

main()

# 6 write a function that returns the reverse of a list
# 7 write a function to find all common elements between two lists
# 8 write a function to move all the elements of a list with value less than 10 to a new list and return it
# 9 write a function to combine two lists into one, alternating elements
    # e.g. combine(['a','b','c'],[1,2,3]) returns ['a', 1, 'b', 2, 'c', 3]