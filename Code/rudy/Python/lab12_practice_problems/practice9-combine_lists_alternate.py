#   Practice 9  Combine Lists Alternating Elements

#Write a function to combine two lists of equal length into one, alternating elements.

#`def combine(nums1, nums2):`

#`combine(['a','b','c'],[1,2,3])` returns `['a', 1, 'b', 2, 'c', 3]`


def combine(list1, list2):
    combined_list = []
    i = 0
    for i in range(len(list1)):         # loops over the indices of the length of a list
        combined_list.append(list1[i])  # appends element of indices in list1 to combined list while i = 0,1,2,3,4....
        combined_list.append(list2[i])  # repeated for list2

    return combined_list


def main():
    list1 = ['A', 'B', 'C', 'D', 'E']
    list2 = [1, 2, 3, 4, 5]

    combined_list = combine(list1, list2)
    print(combined_list)

main()



