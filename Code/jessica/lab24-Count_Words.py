with open('book.txt', 'r') as file:
    text = file.read()
    lower_text = text.lower()

    punctuation = '.,:;![]%'
    for i in range(len(text)):
        remove_punctuation = lower_text.replace(punctuation, ' ')



