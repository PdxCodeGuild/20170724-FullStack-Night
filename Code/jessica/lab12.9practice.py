# 9 write a function to combine two lists into one, alternating elements
# e.g. combine(['a','b','c'],[1,2,3]) returns ['a', 1, 'b', 2, 'c', 3]


def combine(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i])
        new_list.append(list2[i])

    print(new_list)

list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g', 'h']
combine(list1, list2)


