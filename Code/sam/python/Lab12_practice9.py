def combine(list1, list2):              # defining combine function with two parameters
    new_list = []                       # creating a blank list
    for i in range(len(list1)):         # creating a for loop in range of length of list 1
        new_list.append(list1[i])       # appending indexes of list1 to new_list
        new_list.append(list2[i])       # appending indexes of list2 to new_list
    return new_list                     # returning new list to function


def main():
    list1 = [1,2,3,4,5]
    list2 = [7,4,5,3,9]
    print(combine(list1, list2))

main()

