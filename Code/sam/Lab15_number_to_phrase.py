# List of number phrases
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def tens_phrase(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
    if ones_digit == 0:
        return tens[tens_digit]
    else:
        return tens[tens_digit] + '-' + ones[ones_digit]


def hundreds_phrase(num):
    tens_digit = num % 100
    hundreds_digit = num // 100
    hundred_phrase = ones[hundreds_digit] + '-hundred'

    return hundred_phrase + ' ' + tens_phrase(tens_digit)






def main():
    num = int(input('Please input a number: '))
    if num < 100:
        print(tens_phrase(num))
    if num < 1000:
        print(hundreds_phrase(num))

main()



