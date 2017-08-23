# step 2: .pop, step 3: .reverse, step 4, 5, 6: loop, step 7: %
# 1. Convert the input string into a list of ints
# 2. Slice off the last digit.  That is the **check digit**.
# 3. Reverse the digits
# 4. Double every other element in the reversed list.
# 5. Subtract nine from numbers over nine.
# 6. Sum all values.
# 7. Take the second digit of that sum.
# 8. If that matches the check digit, the whole card number is valid.


def convert_credit_card(user_input):
    list_numbers = []
    for i in range(len(user_input)):
        list_numbers.append(int(user_input[i]))
    return list_numbers


def remove_number(list_numbers):
    return list_numbers.pop(len(list_numbers) - 1)


def main():
    card_number = '4556737586899855'
    # card_number = input('Enter credit card number: ')
    conversion = (convert_credit_card(card_number))

    print(conversion)

    check_digit = remove_number(conversion)

    print(conversion)
    print(check_digit)
    conversion.reverse()
    print(conversion)

    for i in range(0, len(conversion), 2):
        conversion[i] *= 2

    print(conversion)

    over_nine = []
    for num in conversion:
        if num > 9:
            over_nine.append(num - 9)
        else:
            over_nine.append(num)

    print(over_nine)

    total = 0
    for num in over_nine:
        total += num
    print(total)

    mod = total % 10

    print(mod)

    if mod == check_digit:
        print('card is valid')
    else:
        print('card is invalid')

main()
