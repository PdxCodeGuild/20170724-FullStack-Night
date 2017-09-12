entering = True
numbers = []
while entering:
    n = input('Enter numbers, when finished type "done": ')
    if n == 'done':
        entering = False
    else:
        numbers.append(int(n))

list_len = len(numbers)

total = 0
for n in numbers:
    total += n
average = total / list_len
print(average)





