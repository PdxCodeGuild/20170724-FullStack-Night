print('Check to see if a word is a palindrome!')

user_input = input('Enter your word here: ')


def check_palindrome(user_input):
    reversed_ui = (user_input[::-1])
    if user_input == reversed_ui:
        print('This is a palindrome.')
    else:
        print('This is not a palindrome.')

check_palindrome(user_input)


print('Check to see if two words are anagrams! ')

user_input1 = input('Enter your first word. ').lower().replace(' ', '')
user_input2 = input('Enter your second word. ').lower().replace(' ', '')


def check_anagram(user_input1, user_input2):
    word1 = str(sorted(user_input1))
    word2 = str(sorted(user_input2))
    if word1 == word2:
        print('This is an anagram.')
    else:
        print('This is not an anagram.')

check_anagram(user_input1, user_input2)