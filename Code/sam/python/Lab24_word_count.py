def calculate_frequency(words):
    word_set = {}
    for word in words:  # iterating over list of words
        if word in word_set:
            word_set[word] = word_set[word] + 1  # if word in word_set, add 1 to value
        else:
            word_set[word] = 1  # if word not in wordset, add to dict and set value to 1



    words = list(word_set.items())
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])


def main():
    with open('alice_in_wonderland.txt', 'r') as file:

        punctuations = "!()[]{};:\"\,<>./?@#$%^&*_~"                    # define punctuations

        phrase_set = {}                                                 # assign empty dictionary to word_set
        text = file.read()                                              # read file, assign to variable name text
        no_punctuations = ''                                            # assign empty string to no_punctuations
        for char in text:                                               # create for loop for character in text
            if char not in punctuations:
                no_punctuations += char                                 # if char NOT punctuation, add to no_punctuations

        lower_case = no_punctuations.lower()                        # converting every letter to lowercase
        words = lower_case.split()                                  # splitting into list of words

        pairs = []
        for i in range(len(words)-1):
            pairs.append(words[i] + ' ' + words[i + 1])             # appending pair of consecutive words in text to pairs list

        user_word = input('Enter a word to find out which words most frequently follow it in the text: ')
        user_word_pairs = []
        for i in range(len(words)- 1):
            if words[i] == user_word:
                user_word_pairs.append(words[i] + ' ' + words[i + 1])


        # print(pairs)
        calculate_frequency(words)
        calculate_frequency(pairs)
        calculate_frequency(user_word_pairs)


main()