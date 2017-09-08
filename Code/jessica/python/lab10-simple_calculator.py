while True:
    operation = input('What is the first operation you want to perform: ')
    if operation == 'done':
        print('goodbye')
        break
    first_number = float(input('What is the first number? '))
    second_number = float(input('What is the second number?'))
    if operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '*':
        print(first_number * second_number)
    elif operation == '/':
        print(first_number / second_number)
