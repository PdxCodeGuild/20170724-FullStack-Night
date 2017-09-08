
i = True
while i:
    user_operator = input('Choose an operator or type "done". ')

    if user_operator == 'done':
        i = False
        print('Goodbye!')
        break
    else:
        number_1 = float(input('What is the first number? '))
        number_2 = float(input('What is the second number? '))

        if user_operator == '+':
            total = number_1 + number_2
            print(total)
        elif user_operator == '-':
            total = number_1 - number_2
            print(total)
        elif user_operator == '*':
            total = number_1 * number_2
            print(total)
        elif user_operator == '/':
            total = number_1 / number_2
            print(total)
        elif user_operator == 'done':
            i = False
            print('Goodbye!')
