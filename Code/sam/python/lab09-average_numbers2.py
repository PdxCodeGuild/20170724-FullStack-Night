
entering = True
numbers = []

while entering:
    n = input('enter a number, when finished type "done: ')
    if n == 'done':
        entering = False
    else:
        numbers.append(int(n))
        print(numbers)

list_len = len(numbers)
total = 0
for n in numbers:
    total += n

av = total / list_len

print(av)

