#    Lab 9.1 Average Numbers

numbers = [4, 8, 12, 2, 10, 7, 1]   # here we have our list called "numbers"

total_numbers = len(numbers)         # variable "list" will hold the length of your elements in or list.

sum = 0                     # sum starts at 0 before adding any numbers to it.

for i in numbers:         # for loop to add num element to the sum until list is complete.
    sum += i             # sum will equal the sum plus next number

average = sum / total_numbers

print('This is the sum of the list: ' + str(sum))
print('This is the total numbers: ' + str(total_numbers))
print('This is the list average: ' + str(average))

