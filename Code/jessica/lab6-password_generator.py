import random

n = input('Enter the length of password: ')

alphabet = 'abcefghijklmnopqrstuvwxyz123456789!@#$%^&*()'
i = 0
password = ''
while i < int(n):
    password = password + str(i)
    print(random.choice(alphabet))
    i = i + 1
print(password)


