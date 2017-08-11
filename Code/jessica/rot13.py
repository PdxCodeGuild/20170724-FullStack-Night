# phrase = 'yynznf'
# phrase.index('y')
# alphabet = alt_alphabet
# alphabet.index('a')


alphabet = 'abcdefghijklmnopqrstuvwxyz'
rot_alphabet = 'nopqrstuvwxyzabcdefghijklm'

phrase = input('Enter phrase ')

# string builder format

def rot13(phrase):
    new_phrase = ''
    for char in phrase:
        index = alphabet.find(char)
        rot_char = rot_alphabet[index]
        new_phrase += rot_char
rot13(phrase)





# translate('yynznf')