amount = int(input('Enter total number in pennies '))

n_quarters = amount // 25
amount -= n_quarters * 25

n_dimes = amount // 10
amount -= n_dimes * 10

n_nickels = amount // 5
amount -= n_nickels * 5

n_pennies = amount


print('Quarters: ' + str(n_quarters))
print('Dimes: ' + str(n_dimes))
print('Nickels: ' + str(n_nickels))
print('Pennies: ' + str(n_pennies))







