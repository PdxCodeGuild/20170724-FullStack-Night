# Write a function that returns the number of occurrences of the 'hi' in a given string.
# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
def count_hi(sentence):
    count = 0
    for i in range(len(sentence)-1):
        if sentence[i] == 'h':
            if sentence[i+1] == 'i':
                # instead of two if stmts could write if sentence[i] == 'h' and i+1 < len(sentence)
                # and sentence [i+1] == 'i':
                # i+1 can be dangerous-possibility of index out of range exception: resolve by not checking last
                # character (range(len(sentence)-1)
                # or can add i +1 < len(sentence) as noted above
                count += 1
    return count


def count_hi2(sentence):
    return count(sentence, 'hi')


def count(sentence, word):  # to generalize have word be parameter
    count = 0
    for i in range(len(sentence)-len(word)+1):  # plus 1 because don't want -3
        # differentiate where you find all characters vs finding one of the characters
        matched = True
        for j in range(len(word)):
            if sentence[i+j] != word[j]:
                matched = False
                break
        if matched:
            count += 1
    return count


def catdog(sentence):
    cat_count = count(sentence, 'cat')
    dog_count = count(sentence, 'dog')
    if cat_count == dog_count:
        return True
    else:
        return False


def main():
    sentence = input('Enter word(s): ')
    print(catdog(sentence))
    print(count_hi2(sentence))

main()