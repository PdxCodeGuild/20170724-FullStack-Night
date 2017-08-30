
def common_elements(list1, list2):
    common = []                         # setting common to a blank list
    for e1 in list1:
        for e2 in list2:                # 'nesting' a for loop inside a for loop
            if e1 == e2:                # comparing element in list1 too element in list2
                common.append(e1)       # if equal, append to common

    return common                       # returning common to function




def main():
    list1 = [1,2,3,4,5]
    list2 = [3,4,5,6,7]
    print(common_elements(list1, list2))


main()
