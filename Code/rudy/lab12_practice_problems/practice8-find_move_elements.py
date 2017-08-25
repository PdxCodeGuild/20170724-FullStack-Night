#   Practice 8


# if variable in [list]:
    # return value


def extract_below10(list_above10):
    i = 0
    list_below10 = []
    for i in list_above10:
        if i < 10:
            list_below10.append(i)

    return list_below10


def main():

    list_above10 = [4, 11, 7, 22, 15, 1]

    list_below10 = extract_below10(list_above10)
    print(list_below10)

main()