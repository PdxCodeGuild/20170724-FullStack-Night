# 7 write a function to find all common elements between two lists
# 2 loops one inside the other
# loop one


def common_elements(list1, list2):
    list3 = []
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                list3.append(num1)
                print(list3)
list1 = [9, 2, 1, 10, 18]
list2 = [2, 5, 1, 9, 17]
common_elements(list1, list2)

