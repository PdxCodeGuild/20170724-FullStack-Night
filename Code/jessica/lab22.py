def check_palindrome():
    word = input('Enter a word: ')
    if word == word[::-1]:
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')
check_palindrome()

def convert_word(word):
    word = word.lower()
    word = word.replace(' ', '')
    word = str(sorted(word))
    return word


def check_anagram(): #str(sorted())
    first_word = input('Enter the first word: ')
    second_word = input('Enter the second word: ')
    first_word = convert_word(first_word)
    second_word = convert_word(second_word)
    if first_word == second_word:
        print('they are anagrams.')
    else:
        print('they are not anagrams.')

check_anagram()



