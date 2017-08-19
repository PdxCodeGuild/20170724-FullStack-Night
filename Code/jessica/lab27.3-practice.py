# Write a function that takes a string, and returns a list of strings, each missing a different character.
def missing_char(word):
    list_words = []
    list_words.append(word)
    list_words.append(word[1:])

    new_word = ''
    for i in range(len(word) - 1):  # HELP! I can't seem to figure this out
        new_word += word[i]
    list_words.append(new_word)

    print(list_words)


missing_char('kitten')


# def main():
#     word = input('Enter a word: ')
#     print(missing_char(word))
#
# main()