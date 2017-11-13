#   Practice 7  Common Elements Between Two Lists


def common_elements(list_1, list_2):
    n_matches = 0
    common_list = []
    for num in list_1:
        for numx in list_2:
            if num == numx:
                common_list.append(num)
                print(common_list)
                n_matches += 1
    return n_matches


def main():
    list_1 = ['a', 'b', 'c', 'd', 'e']
    list_2 = ['d', 'b', 'b', 'f', 's']
    n_matches = common_elements(list_1, list_2)
    print(n_matches)

main()



