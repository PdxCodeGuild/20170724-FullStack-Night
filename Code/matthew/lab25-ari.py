

file_name = 'the_flower_princess.txt'
with open(file_name, 'r') as f:
    text = f.read()

    n_sentences = 0
    for char in text:
        if char == '.':
            n_sentences += 1

    text = text.replace('\n', ' ')
    text = text.replace('\'', '')
    words = text.split(' ')
    n_words = len(words)

    n_characters = 0
    # for word in words:
    #    n_characters += len(word)

    for word in words:
        for char in word:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                n_characters += 1

    ari = 4.71*(n_characters/n_words) + 0.5*(n_words/n_sentences)-21.43
    ari = int(ari + 0.5)
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
    print(ari_scale[ari])








