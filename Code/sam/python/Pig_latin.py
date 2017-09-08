user_input = input('Word? ')


first_letter = user_input[0]
rest_of_word = user_input[1:]

vowels = 'aeiou'


# word not starting with a vowel
if first_letter not in vowels:
    output = '{}{}ay'.format(rest_of_word, first_letter)
elif first_letter in vowels:
    output = '{}{}yay'.format(rest_of_word, first_letter)
print(user_input + ' In pig latin is ' + output)

