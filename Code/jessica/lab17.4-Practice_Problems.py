# Get a string from the user, print out another string, doubling every letter.

word = input('Enter some text: ')
new_word = ''
for letter in word:
    new_word += letter + letter

print(new_word)