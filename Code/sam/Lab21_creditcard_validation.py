
def convert_user_input(card_number):                # creating a function to convert cc #
    new_list = []                                   # assigning a blank list to new_list
    for i in range(len(card_number)):
        new_list.append(int(card_number[i]))        # appending int of [i] to new_list
    return new_list


def elements_doubled(reversed_list):                # creating a function to double elements
    for i in range(len(reversed_list)):
        if i % 2 == 0:                              # using % to get every other element and * 2
            reversed_list[i] *= 2


def subtract_nine(new_list):                        # function to - 9 from elements > 9
    subtract_nine_list = []
    for num in new_list:                            # iterating over elements in new_list
        if num > 9:
            subtract_nine_list.append(num - 9)      # appending element - 9 if element > 9
        else:
            subtract_nine_list.append(num)          # else just appending element to list
    return subtract_nine_list                       # returning list to function










def main():
    card_number = '4556737586899855'
    # card_number = input('Enter your credit card number: ')
    new_list = convert_user_input(card_number)      # assigning function to new_list

    print(new_list)

    check_digit = new_list.pop(-1)            # assigning last item of new_list to check_digit
    print(new_list)

    new_list.reverse()                        # reversing new_list
    print(new_list)

    elements_doubled(new_list)                # calling elements_doubled
    print(new_list)

    subtract_nine_list = subtract_nine(new_list)
    print(check_digit)

    total = 0                                 # assigning 0 to total
    for num in subtract_nine_list:
        total += num                          # adding each element of list to total
    print(total)

    second_digit = total % 10                 # using mod to get second digit of total

    if second_digit == check_digit:           # comparing second_digit to check_digit
        print('Valid!')                       # if True print valid
main()