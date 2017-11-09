# Lab 7 Make Change

#We want to ask for the amount of money from the user. Convert that number into an int with floating decimal place to the hundreth place. Once we convert that, we want to divide the dollar amount by 25 to get the most amount of quarters. The remaining change will replace the amount of money that we need to divide by 10 to get the dimes. Continue same process to get nickely and the remaining number will equal the amount of pennies.

# version #1
money = input('Please give me the amount of money you would like to convert into change. $') # User inputs number.
money = int(float(money)*100)
# we are turning user's input number and turning it from a string into an integer.
# Then by using the function float(money) and multiplying it by 100.
# We are representing the total amount of money converted in pennies.
# $1.49 = 149 pennies.

print('Your change in pennies is ' + str(money)) # this is the amount of pennies total

# version #2

quarters = money // 25  #establishing a variable named "quarters" equals total pennies divided by 25. (The value of a quarter in pennies.)
money = money - quarters*25 # we are subtracting the total number of quarters from money (the total number of pennies) to create a new value for money.
# variable "money" now equals the remaining amount of pennies after all quarters have been calculated.

print('You have this many quarters: ' + str(quarters))

dimes = money // 10 # see quarters
money = money - dimes*10

print('You have this many dimes: ' + str(dimes))

nickels = money // 5 # see quarters
money = money - nickels*5

print('You have this many nickels: ' + str(nickels))

pennies = money

print('You have this many pennies: ' + str(pennies))
