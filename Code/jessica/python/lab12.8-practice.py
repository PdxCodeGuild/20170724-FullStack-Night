# 8 write a function to move all the elements of a list with value less than 10 to a new list and return it
def extract_less_than_ten(list):
    new_list = []
    for num in list:
        if num < 10:
            new_list.append(num)
            print(new_list)

list = [4, 16, 20, 9, 7]
extract_less_than_ten(list)
