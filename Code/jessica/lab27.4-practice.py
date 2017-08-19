# Write a function that returns the number of occurrences of the 'hi' in a given string.
def count_hi(word):
    count = 0
    for i in range(len(word)):
        if word[i] == 'h':
            if word[i+1] == 'i':
                count += 1
    return count


def main():
    word = input('Enter word(s): ')
    print(count_hi(word))

main()