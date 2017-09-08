# x = 123 print(x //100) print(x//10%10) print(x%10)

# convert to english
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero-placeholder', 'one-placeholder', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def get_tens_phrase(number):
    if number < 10:
        return ones[number] # use the number as the index
    elif number < 20:
        return teens[number - 10]
    elif number < 100:
        tens_digit = number // 10  # number floor division 10 --> drops remainder ie: 10 // 10 = 1
        ones_digit = number % 10  # number mod 10 --> gives remainder ie: 10 % 10 = 0
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + ones[ones_digit]


def get_hundreds_phrase(number):
    hundreds_digit = number // 100  # number floor division 100 ie: 100 // 100 = 1
    tens_digit = number % 100  # number mod 100 ie: 100 % 100 = 0
    hundreds_phrase = ones[hundreds_digit]+'hundred'
    if tens_digit == 0:
        return hundreds_phrase
    else:
        return hundreds_phrase + ' ' + get_tens_phrase(tens_digit)


def get_thousands_phrase(number):
    thousands_digit = number // 1000 # number floor division 1000 ie: 1000 // 1000 = 1
    hundreds_digit = number % 1000  # number mod 1000 ie: 1000 % 1000 = 0
    thousands_phrase = ones[thousands_digit]+'thousand'
    if hundreds_digit == 0:
        return thousands_phrase
    else:
        return thousands_phrase + ' ' + get_hundreds_phrase(hundreds_digit)


def main():
    # get the number from the user: handles numbers 100-999
    number = int(input('what is the number? '))
    if number < 100:
        print(get_tens_phrase(number))
    elif number < 1000:
        print(get_hundreds_phrase(number))
    else:
        print(get_thousands_phrase(number))
main()




