#   Lab 17.2    Print with 'While' Loop then 'For' Loop


def every_other_while(list1):
    i = 0
    while_list = []
    while i < len(list1):
        while_list.append(list1[i])
        i += 2

    return while_list


def every_other_for(list1):
    i = 0
    for_list = []
    for i in range(0, len(list1), 2):
        for_list.append(list1[i])

    return for_list

'''
     i = 0
        for_list = []
        for i in range(0, len(list1)):
            if i % 2 == 0:
                for_list.append(list1[i])
    
        return for_list
'''
'''
    i = 0
    for_list = []
    for i in range(len(list1)):
        if i % 2 == 0:
            for_list.append(list1[i])
    
    return for_list
'''


def main():
    list1 = ['A', 'B', 'C', 'D', 'E', 'F']

    while_list = every_other_while(list1)
    for_list = every_other_for(list1)
    print(while_list)
    print(for_list)

main()

