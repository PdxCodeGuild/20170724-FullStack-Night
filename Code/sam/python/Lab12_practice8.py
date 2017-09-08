def extract_less_than_10(list):      # defining extract_less_than_10 function with 1 parameter
    new_list = []                    # creating a new list
    for e in list:                   # for element in list
        if e < 10:                   # if element is less than 10
            new_list.append(e)       # append element to new list
    return new_list                  # return new list to function




def main():
    list = [3,5,7,11,13]
    print(extract_less_than_10(list))

main()