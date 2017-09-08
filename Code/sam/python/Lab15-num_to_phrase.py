
def tens(first_dec):                   # defining function for tens digit

    if first_dec == 9:
        return 'ninety-'
    if first_dec == 8: 
        return 'eighty-'
    if first_dec == 7: 
        return 'seventy-'
    if first_dec == 6:
        return 'sixty-'
    if first_dec == 5:
        return 'fifty-'
    if first_dec == 4: 
        return 'forty-'
    if first_dec == 3:
        return 'thirty-'
    if first_dec == 2:
        return 'twenty-'


def ones(second_dec):                    # defining function for ones digit

    if second_dec == 9:
        return 'nine'
    if second_dec == 8: 
        return 'eight'
    if second_dec == 7: 
        return 'seven'
    if second_dec == 6: 
        return 'six'
    if second_dec == 5:
        return 'five'
    if second_dec == 4:
        return 'four'
    if second_dec == 3:
        return 'three'
    if second_dec == 2:
        return 'two'
    if second_dec == 1:
        return 'one'


def main():
    user_number = int(input('What is your number? '))

    first_dec = user_number // 10
    second_dec = user_number % 10

    teens_list = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    if user_number < 10:
        print(ones(user_number))
    elif user_number < 20:
        teens = (teens_list[user_number - 10])
        print(teens)
    elif user_number < 100:
        print(tens(user_number) + ones(user_number))


main()



