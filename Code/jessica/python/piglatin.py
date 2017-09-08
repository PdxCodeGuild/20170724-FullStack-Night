word = input('Please provide a word ')

#access by index
first_letter = word[0]
rest_of_word = word[1:]

vowels = 'aeiou'

#if-else to determine first letter of word
if first_letter in vowels:
    output = '{}yay'.format(rest_of_word, first_letter)
    print(output)
else:
    output = '{}{}ay'.format(rest_of_word, first_letter)
    print(output)





