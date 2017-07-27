
n_quarters = 0
n_dimes = 0
n_nickels = 0
n_pennys = 0

amount = input('enter the amount in dollars: ')
amount = int(float(amount) * 100)


amount >= 25
n_quarters = amount // 25
amount -= n_quarters*25

amount >= 10
n_dimes = amount // 10
amount -= n_dimes*10

amount >= 5
n_nickels = amount // 5
amount -= n_nickels*5

amount >= 1
n_pennys = amount // 1
amount -= n_pennys


print('number of quarters:' + str(n_quarters))  #str() converts int to string
print('number of dimes:' + str(n_dimes))
print('number of nickels:' + str(n_nickels))
print('number of pennys:' + str(n_pennys))
