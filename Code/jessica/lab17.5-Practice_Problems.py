# Write a function that merges two lists into a single list, where each element of the outlist list
# is another list containing two elements.

list1 = [5, 2, 1]
list2 = [6, 8, 2]

def merge(list1, list2):
    new_list = []
    for i in range(len(list1)):                    # don't loop through both
        new_list.append((list1[i], list2[i]))  # append item 1 from list 1 and 2, then append item 2 from list 1 and 2 and so forth
    print(new_list)

merge(list1, list2)




