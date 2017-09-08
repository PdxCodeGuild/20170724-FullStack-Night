user_input = input('What was your number grade? ')
user_input = int(user_input)

if user_input >= 90:
    print('You got an A!')
elif user_input >= 80:
    print('You got a B!')
elif user_input >= 70:
    print('You got a C!')
elif user_input >= 60:
    print('You got a D!')
else:
    print('You got an F.')