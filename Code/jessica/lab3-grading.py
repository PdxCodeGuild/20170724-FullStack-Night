x = int(input ('Enter a number representing the grade (0-100):'))

if x > 90:
    print('The grade is an A')
elif x >= 80 and x <=89:
    print('The grade is a B')
elif x >= 70 and x <= 79:
    print('The grade is a C')
elif x >= 60 and x <= 69:
    print('The grade is a D')
else:
    print('The grade is an F')

