# Lab 9.2 Average Numbers

numbers_list = [ ]          # variable assigned to an empty list
listing = True              # variable listing is assigned a True boolean value#
#n = sum                     # variable
sum = 0

while listing:
    n = input('Enter a number or "done": ')
    if n == str('done'):
        listing = False
    else:
        numbers_list.append(int(n))


print('You have ' + str(len(numbers_list)) + ' numbers in your list.')
print(numbers_list)
for n in numbers_list:
    sum += n
#print(sum)

average = sum / len(numbers_list)

#print('Your list of numbers is ' + str(numbers_list))
print('The average of the numbers in your list is ' + str(average))
