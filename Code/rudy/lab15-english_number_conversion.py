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
        ones = ones_english[ones_x]

        return tens + ' ' + ones

    elif x > 100:
        hundreds_x = (x//100) - 1
        if x == 0:
            x + 1
            hundred = ones_english[hundreds_x]
            print(hundred)


def main():
    x = int(input('Enter a number between 1-99 -> '))

    eng_conversion = num2eng_conversion(x)
    print(eng_conversion)

main()

