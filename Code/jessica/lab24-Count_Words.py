def calc_freq(words):
    word_set = {}
    for j in range(len(words)):
        if words[j] == '':
            continue
        if words[j] not in word_set:
            word_set[words[j]] = 1
        else:
            word_set[words[j]] += 1
    words = list(word_set.items())
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    print(words)
    return words


def parse_txt(path):
    with open('book2.txt', 'r') as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        words = text.split(' ')

        pairs = []
        for i in range(len(words)):
            words[i] = words[i].strip('.,;')
        for i in range(len(words)-1):
            if words[i] == '':
                continue
            pairs.append(words[i] + ' ' + words[i+1])

        calc_freq(words)
        pair_set = calc_freq(pairs)

        choose_word = input('Enter a word from the text: ')
        # for i in range(len(pairs)):
        #     if pairs[i].startswith(choose_word):
        #         print(pairs[i])
        counter = 10
        for pair in pair_set:
            if choose_word == pair[0].split(' ')[0]:
                print(pair)
                counter -= 1
                if counter == 0:
                    break
parse_txt('book2.txt')






