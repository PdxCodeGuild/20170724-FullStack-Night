# Write a function that takes a string, and returns a list of strings, each missing a different character.
def missing_char(word):
    list_words = []
    for i in range(len(word)):
        list_words.append(word[:i] + word[i + 1:])
    return list_words


def main():
    word = input('Enter a word: ')
    print(missing_char(word))

main()

