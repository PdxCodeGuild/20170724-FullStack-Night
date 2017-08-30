def parse_txt(path):
    import math

    with open(path, 'r') as file:
        text = file.read()
        text = text.lower()
        text = text.replace('\n', ' ')
        words = text.split(' ')
        punctuation = '!@#$%^&*()><,;:-'

        # to remove punctuation
        no_punct = ''
        for char in text:
            if char not in punctuation:
                no_punct += char

        sentence_count = 0
        for char in no_punct:
            if char == '.':
                sentence_count += 1


        word_count = 0
        for word in words:
            if word != '':
                word_count += 1
        #print(word_count)

        #character_count = 0
        #for word in words:
        #    bad_chars = '-\'\".:;/'
        #    for bad_char in bad_chars:
        #        word = word.replace(bad_char, '')
        #    character_count += len(word)

        #character_count = 0
        #for i in range(len(words)):
        #    words[i] = words[i].strip('.,;:')
        #    if words[i] != ' ':
        #        character_count += 1
        #print(character_count)

        # loop through the words
        # for each word, loop through the characters of the word
        # if the character is inside a string representing the alphabet
        # increment the character count
        character_count = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for word in words:
            for char in word:
                if char in alphabet:
                    character_count += 1
        #print(character_count)

        # 4.17 * (number of characters / # of words) +.5 (number of words/number of sentences) - 21.43
        score = 4.17*(character_count / word_count) + .5*(word_count / sentence_count) - 21.43
        #score = int(score + .5)
        score = math.ceil(score)
        #print(score)

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

        grade_scale = ari_scale[score]
        #print(grade_scale)

        output = ' ----------------------------------------------------------\n'  # output ='-'*80 + '\n'
        output += '\tThe ARI for ' + path + ' is ' + str(score) + '.\n'
        output += '\tThis corresponds to a ' + grade_scale['grade_level'] + ' level of difficulty.\n'
        output += '\tThat is suitable for an average person ' + grade_scale['ages'] + ' years old.\n'
        output += ' ----------------------------------------------------------\n' # output ='-'*80

        print(output)

parse_txt('book2.txt')



