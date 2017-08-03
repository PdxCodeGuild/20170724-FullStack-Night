phrase = 'yynznf'
phrase.index('y')

#alphabet = alt_alphabet
#alphabet.index('a')


def translate(phrase: str) -> str:
    """
    Takes in alt_alphabet and translates to alphabet
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alt_alphabet = 'nopqrstuvwxyzabcdefghijklm'
    phrase = ''
    for char in phrase:
        ind = alphabet.index(char)
        print(alt_alphabet[ind])
        phrase += alt_alphabet
        print(phrase)







    #translate('yynznf')