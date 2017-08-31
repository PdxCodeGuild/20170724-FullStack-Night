#   Lab 15  Converting Number to English


# x = 67
#(x//10)
#(x%10)


def num2eng_conversion(x):
    ones_english = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens_english = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens_english = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if x < 10:
        ones = ones_english[x]

        return ones

    elif 10 <= x < 20:
        x -= 10
        tens_x = teens_english[x]
        ones = tens_x

        return ones

    elif x < 100:
        tens_x = (x//10) - 2
        tens = tens_english[tens_x]
        ones_x = x % 10
        if ones_x == 0:
            ones = ''
        else:
            ones = ones_english[ones_x]

        return tens + ' ' + ones

    elif x > 100:                   # hypothetical x = 123
        hundreds_x = (x//100)       # floor division removes remainder and gives you the 100
        hundred_tens_x = (x % 100)    #
        print(hundreds_x)
        print(hundred_tens_x)
        if hundreds_x >= 1:
            hundreds = str(ones_english[hundreds_x] + ' hundred')

            if hundred_tens_x < 10:
                over_hundred = ones_english[hundred_tens_x]

            elif 10 <= hundred_tens_x < 20:
                hundred_tens_x -= 10
                tens_x = teens_english[hundred_tens_x]
                over_hundred = tens_x

            elif hundred_tens_x < 100:
                tens_x = (hundred_tens_x // 10) - 2
                tens = tens_english[tens_x]
                ones_x = x % 10
                if ones_x == 0:
                    ones = ''
                else:
                    ones = ones_english[ones_x]
                over_hundred = f'{tens}-{ones}'

            return f'{hundreds} {over_hundred}'


def main():
    x = int(input('Enter a number between 1-999 -> '))

    eng_conversion = num2eng_conversion(x)
    print(eng_conversion)

main()

