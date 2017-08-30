
def reversed_list(nums):
    list = []                       # setting list to a blank list
    for e in nums:                  # for element in list nums
        list.insert(0, e)           # insert element at index 0 of nums
    return list                     # return list to function




def main():
    nums = [1,2,3,4,5]
    print(reversed_list(nums))


main()








# def reverse_list(nums):
#     reversed_num = list(reversed(nums))
#     return reversed_num
#
#
# def main():
#     nums = [3, 2, 5, 9, 7]
#     print(reverse_list(nums))
#
#
# main()


