# Lab 10.1 Simple Calculator


user_input = input('Please choose and operator like + - * / ')
var1 = float(input('What is the first number? '))     # using float so you can use decimal places
var2 = float(input('What is the second number? '))

if user_input == '+':       # using if statement to determine which input user typed in
    print(var1 + var2)          # if user chose the string '+' then we are adding the variables
elif user_input == '-':
    print(var1 - var2)
elif user_input == '*':
    print(var1 * var2)
elif user_input == '/':
    if var1 == 0 or var2 == 0:
        print('Answer is undefined, cannot divide by zero.')
    else:
        print(var1 / var2)
else:
    print('Unknown operator.')




