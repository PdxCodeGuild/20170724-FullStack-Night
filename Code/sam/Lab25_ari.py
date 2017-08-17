path = 'alice_in_wonderland.txt'
with open(path, 'r') as file:
    punctuations = '\'!()[]{};:"-\,<>./?@#$%^&*_~'
    text = file.read()
    sentence_count = 0
    word_count = 0
    char_count = 0
    for char in text:                                          # sentence counter
        if char == '.':
            sentence_count += 1
    lower_case = text.lower()                                  # changing text to lowercase
    no_punct = ''
    for char in lower_case:                                     # getting rid of punctuations
        if char not in punctuations:
            no_punct += char
    words = no_punct.split()
    for word in words:                                          # word counter
        word_count += 1
    for word in words:
        for char in word:
            char_count += 1

    import math
    ari = ((4.71 * char_count / word_count + 0.5 * word_count / sentence_count - 21.43))
    ari = math.ceil(ari)
    print(ari)

    ari_scale = {
         1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
         2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
         3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
         4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
         5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
         6: {'ages': '10-11', 'grade_level':    '5th Grade'},
         7: {'ages': '11-12', 'grade_level':    '6th Grade'},
         8: {'ages': '12-13', 'grade_level':    '7th Grade'},
         9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

    grade_level = ari_scale[ari]
    print(grade_level)

    output = ''
    output += 'The ARI for ' + path + ' is ' + str(ari) + '. \n'
    output += 'This corresponds to the ' + grade_level['grade_level'] + ' level of difficulty.\n'
    output += 'That is suitable for an average person ' + grade_level['ages'] + ' years old.\n'
    print(output)


