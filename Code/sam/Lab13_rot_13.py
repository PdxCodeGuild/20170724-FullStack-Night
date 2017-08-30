

def rot13(user_string):                              # defining the function for rot13
    encrypted = ''                                   # creating a blank str
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'
    for char in user_string:
        char_index = alphabet.find(char)             # finding index of element in alphabet str
        rotated_char = alphabet_rotated[char_index]  # using char_index to find element in a_r
        encrypted = encrypted + rotated_char         # adding element to empty str (same as +=)

    return encrypted                                 # returning encrypted to function


def main():
    user_string = input('Type the message you want encrypted: ')
    print('Here is your encrypted message: ' + rot13(user_string))  # string concatenation


main()                                               # calling main function