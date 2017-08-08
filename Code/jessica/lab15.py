# x = 123
# print(x //100)
# print(x//10%10)
# print(x%10)


# get the number from the user: handles numbers 0-99
number = int(input('Enter a number. '))

# get the ones digit and the tens digit from the number
ones_digit = number % 10
tens_digit = number // 10

# convert that to english
# use a list use the ones digit or the tens digit to look up index
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ones_word = words[ones_digit]

teen_words = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
teens = teen_words[ones_digit]

tens_words = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
tens = tens_words[tens_digit - 2]

# if ones_digit <= 9 and tens_digit < 1:
#    print(ones_word)
# elif tens_digit == 1:
#    print(teens)
# elif tens_digit >= 2 and ones_digit >= 1:
#    print(tens + ones_word)
# else:
#    print(tens)

if number <= 9:
    print(ones_word)
elif 10 < number < 19:
    print(teens)
elif number >= 20:
    print(tens + ones_word)
elif number >= 20 and ones_digit == 0:
    print(tens)



