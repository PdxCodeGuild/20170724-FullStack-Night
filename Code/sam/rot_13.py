

def rot13(user_string):                                      # defining the function for rot13
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'
    for char in user_string:                                  # creating a for loop
        char_index = alphabet.find(char)                      # finding the index of element in alphabet string
        rotated_char = alphabet_rotated[char_index]
        encrypted = encrypted + rotated_char

    return encrypted


def main():
    user_string = input('Type the message you want encrypted: ')
    print('Here is your encrypted message: ' + rot13(user_string))


main()