#   Lab 13.1 ROT Cipher

# Write a program that decrypts a message encoded with ROT13 on each character starting with 'a', and displays it to the user in the terminal.

# start with a blank output string
# loop through every character of the string tht the user entered
# find the index of that character in the alphabet
# using that index, find the character in the rotated alphabet
# append that character to the output string

def rot13(user_string):
    alphabet =         'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'
    # print(user_string)

    user_string13 = ''
    for i, char in enumerate(user_string):
        # print(str(i) + ' ' + str(char))
        index_user = alphabet.find(char)
        # print(index_user)
        char_rot = alphabet_rotated[index_user]

        user_string13 += char_rot
    return user_string13


def main():
    user_string = input('Enter the message you would like to encrypt here: ')


    user_string13 = rot13(user_string)
    print(user_string13)



main()



'''
VERSION 2
how to wrap around to the beginning of the alphabet

def rotn(user_input):

for char in user_input:
    index = alphabet.find(char)
    index += 13                     # rotates the alphabet 13 indices
    if index >= len(alphabet):      # if the index extends past the length of the alphabet
        index -= len(alphabet)
    output += alphabet[index]
    print(output)    
'''