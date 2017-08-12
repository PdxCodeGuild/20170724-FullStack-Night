
def list_merge(list_1, list_2):
    # LIST BUILDER PATTERN
    new_list = []
    for i in range(len(list_1)):
        new_list.append([list_1[i], list_2[i]])    # appending list of two elements to new list
    return new_list


def main():
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    print(list_merge(list_1, list_2))


main()
