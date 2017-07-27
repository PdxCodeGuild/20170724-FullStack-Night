
import random

alphabet = '0123456789!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
i = 0
n = 10
password = ''
while i < n:
    password += random.choice(alphabet)
    i += 1
print(password)
