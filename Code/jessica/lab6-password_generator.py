import random

n = input('Enter the length of password: ')

alphabet = 'abcefghijklmnopqrstuvwxyz123456789!@#$%^&*()'
i = 0
password = ''
while i < int(n):
    password += random.choice(alphabet)
    i += 1

print(password)


