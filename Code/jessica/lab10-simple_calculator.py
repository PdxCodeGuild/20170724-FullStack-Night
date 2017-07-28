def x():
    print(input('What is the first operation you want to perform: '))


def a():
    print(float(input('What is the first number: ')))


def b():
    print(float(input('What is the second number: ')))


entering = True
numbers = []
while entering:
    if x == ('+', '-', '/', '*'):
        print(a())
    elif a() == int:
        print(b())
    else:
        print('try again')


# def add():
#     return a + b
# def subtract():
#     return a - b
# def multiply():
#     return a * b
# def divide():
#     return a / b

