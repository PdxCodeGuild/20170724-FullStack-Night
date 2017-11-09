# Lab 10.2    Simple Calculator


using_calculator = True

while using_calculator:
    user_input = input('Please choose an operation (+ - * /) ')

    var1 = float(input('Please the first number '))
    var2 = float(input('Please the second number '))
    var3 = 0
    if user_input == 'done':
        break
    elif user_input == '+':  # using if statement to determine which input user typed in
        print(var1 + var2)  # if user chose the string '+' then we are adding the variables
    elif user_input == '-':
        print(var1 - var2)
    elif user_input == '*':
        print(var1 * var2)
    elif user_input == '/':
        print(var1 / var2)
    else:
        print('Unknown operator.')




