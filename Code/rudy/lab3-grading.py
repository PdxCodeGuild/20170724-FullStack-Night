score = input('Please input your score (0-100) here ')

x = score
x = int(x)
if x >100:
    print('Sorry. That is not a valid score. You failed, try again.')
elif x > 90:
    print('You scored an A')
elif x > 80:
    print('You scored an B')
elif x > 70:
    print('You scored an C')
elif x > 60:
    print('You scored an D')
else:
    print('You scored an F')


