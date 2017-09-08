nums_list = []                                             # creating a blank list

while True:
    user_input = input('Enter a number, or type done. ')
    if user_input == 'done':
        print(nums_list)
    else:
        nums_list.append(user_input)                        # appending user_input to nums_list

