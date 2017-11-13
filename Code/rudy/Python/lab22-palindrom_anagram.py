#   Lab 22  Palindrom and Anagram


def reverse_word(word):
    rev_word = (word[::-1])
    return rev_word


def check_palindrome(word):
    word_orig = word
    word = word.replace(' ', '')
    rev_word = reverse_word(word)
    if word == rev_word:
        print(f'{word_orig} is a Palindrome!')
    else:
        print(f'nothing special about \'{word_orig}\'')


def check_anagram(word1, word2):
    word1_orig = word1
    word2_orig = word2
    word1 = word1.replace(' ', '')
    word2 = word2.replace(' ', '')
    word1_list = list(word1)
    word2_list = list(word2)
    word1_list.sort()
    word2_list.sort()
    if word1_list == word2_list:
        return print(f'{word1_orig} & {word2_orig} make an anagram!!!')
    else:
        return print(f'nothing special about \'{word1_orig} & {word2_orig}\'')



def main():
    action = input('Welcome to the Palin-gram check!\n'
                  'Check for Palindrome or Anagram? ').lower()

    if str(action[0]) == 'p':
        word = input('Type word here ').lower()
        action = 'palindrome'
        print('...checking word for palindrome...')
        check_palindrome(word)
    if str(action[0]) == 'a':
        word1 = input('Type word here ').lower()
        word2 = input('Type word here ').lower()
        action = 'anagram'
        print('...checking word for anagram...')
        check_anagram(word1, word2)



main()
