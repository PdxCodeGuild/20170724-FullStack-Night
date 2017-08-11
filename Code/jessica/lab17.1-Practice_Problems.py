# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.


numbers = []
while True:
    x = input('Enter a number (or done): ')
    if x == 'done':
        break
    else:
        numbers.append(x)
print(numbers)