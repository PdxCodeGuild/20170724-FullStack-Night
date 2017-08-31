#   Lab 25  ARI Formula

# ARI Formula = (4.71(character/words)) + (0.5(words/sentences)) - 21.43

import math


def sentence_counter(text):
    sentence_count = 0
    for words in text:
        for char in words:
            if char == '.':
                sentence_count += 1
    return sentence_count


def char_counter(text):
    alphabet = ['abcdefghijklmnopqrstuvwxyz']
    char_count = 0
    for words in text:
        for char in words:
            i = 0
            if words[i] in alphabet[i]:
                char_count += 1
    return char_count


def word_counter(words):
    word_count = 0
    for word in words:
        if word != '':
            word_count += 1
    return word_count


def parse_txt(path):
    with open(path, 'r') as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        text = text.replace('a.d.', 'ad')
        text = text.replace('  ', ' ')
        words = text.split(' ')
    return words


def main():
    path = 'meditations.txt'
    text = parse_txt(path)
    print(f'The following counts are for the text {path}')
    char_count = char_counter(text)
    print(f'Character count: {char_count}')

    word_count = word_counter(text)
    print(f'Sentences count: {word_count}')

    sentence_count = sentence_counter(text)
    print(f'Sentences count: {sentence_count}')

    # ARI Formula = (4.71(character/words)) + (0.5(words/sentences)) - 21.43

    x = char_count/word_count
    x *= 4.71
    y = word_count/sentence_count
    y *= 0.5
    ari_score = math.ceil((x + y)-21.43)

    ari_scale = {
        1: {'ages': '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages': '6-7', 'grade_level': '1st Grade'},
        3: {'ages': '7-8', 'grade_level': '2nd Grade'},
        4: {'ages': '8-9', 'grade_level': '3rd Grade'},
        5: {'ages': '9-10', 'grade_level': '4th Grade'},
        6: {'ages': '10-11', 'grade_level': '5th Grade'},
        7: {'ages': '11-12', 'grade_level': '6th Grade'},
        8: {'ages': '12-13', 'grade_level': '7th Grade'},
        9: {'ages': '13-14', 'grade_level': '8th Grade'},
        10: {'ages': '14-15', 'grade_level': '9th Grade'},
        11: {'ages': '15-16', 'grade_level': '10th Grade'},
        12: {'ages': '16-17', 'grade_level': '11th Grade'},
        13: {'ages': '17-18', 'grade_level': '12th Grade'},
        14: {'ages': '18-22', 'grade_level': 'College'}
    }

    ari_grade = ari_scale[ari_score]

    print(f'\n''The ARI for {path} is ' + str(ari_score))
    print(f'This corresponds to a ' + ari_grade['grade_level'] + ' level of difficulty\n''that is suitable for an average person ' +             ari_grade['ages'] + ' years old.')


main()
