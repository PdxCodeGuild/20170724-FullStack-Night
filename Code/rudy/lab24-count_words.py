#   Lab 24  Count Words


def parse_txt(path):
    with open('meditations.txt', 'r') as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.split(' ')
        for i in range(len(text)):
            text[i] = text[i].strip('.,!@#$%^&*()_-ï»¿')

        meditation = {}
        for word in text:
            if word in meditation:
                meditation[word] = meditation[word] + 1
            else:
                meditation[word] = 1
    return meditation, text


def frequency_top10(meditation):
    words = list(meditation.items())
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])
    return words


def frequency(meditation):
    pass


def main():
    meditation, text = parse_txt('meditations.txt')
    print(text)
    pair = []

    pairs = {}
    for i in range(len(text)-1):
        pair.append(text[i] + ' ' + text[i+1])
    print(pair)

    for pair_words in pair:
        if pair_words in pairs:
            pairs[pair_words] = pairs[pair_words] + 1
        else:
            pairs[pair_words] = 1



main()



