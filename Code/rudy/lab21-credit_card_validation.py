#   Lab 21  Credit Card Validation

'''
1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.
'''


def convert_int_list(card_number):
    cc_list = []
    for i in card_number:
        i = int(i)
        cc_list.append(i)

    return cc_list


def reverse_list(sliced_cc):
    rev_cc = []
    for num in sliced_cc:
        #  print(rev_nums)
        rev_cc.insert(0, num)

    return rev_cc


def double_element(rev_cc):
    #dub_list = []
    for i in range(len(rev_cc)):
        if i % 2 == 0:
            rev_cc[i] *= 2

    return rev_cc


def sub_nine(dub_list):
    sub_nine_list = []
    for i in dub_list:
        if i > 9:
            i -= 9
        sub_nine_list.append(i)

    return sub_nine_list


def sum_num(sub_nine_list):
    pass


def main():
    card_number = input('Please input you 16 digit card number: ')
    #print(card_number)

    cc_list = convert_int_list(card_number)
    print(cc_list)

    check_digit = cc_list[14:15][0]

    print(f'This is the check digit: {check_digit}')

    sliced_cc = cc_list[0:15]
    print(sliced_cc)

    rev_cc = reverse_list(sliced_cc)
    print(rev_cc)

    dub_list = double_element(rev_cc)
    print(dub_list)

    sub_nine_list = sub_nine(dub_list)
    print(sub_nine_list)

    sum_all = sum(sub_nine_list)
    print(sum_all)

    x = sum_all % 10
    print(x)

    if sum_all % 10 == check_digit:
        print('Valid!')
    else:
        print('Not Valid!')


main()



