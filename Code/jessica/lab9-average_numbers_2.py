entering = True
numbers = []
while entering:
    n = input('Enter numbers, when finished type "done": ')
    if n == 'done':
        entering = False
    else:
        numbers.append(int(n))

    print(numbers)




