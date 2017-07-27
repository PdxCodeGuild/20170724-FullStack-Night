amount = input('Enter total number in pennies ')

n_quarters = int(amount) // 25
n_dimes = (int(amount) - int(n_quarters) * 25) // 10
n_nickels = (int(amount) - int(n_quarters) * 25 - int(n_dimes) * 10) // 5
n_pennies = (int(amount) - int(n_quarters) * 25  - int(n_dimes) * 10 - int(n_nickels) * 5) // 1

print(n_quarters)
print(n_dimes)
print(n_nickels)
print(n_pennies)







