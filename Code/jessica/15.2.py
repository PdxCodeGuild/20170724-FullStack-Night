# x = 123
# print(x //100)
# print(x//10%10)
# print(x%10)


# get the number from the user: handles numbers 100-999
number = int(input('Enter a number. '))

# get the ones digit and the tens digit from the number
ones_digit = number % 10
tens_digit = number // 10 % 10
hundreds_digit = number // 100

# convert that to english
# use a list use the ones digit and the tens digit to look up index
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def get_tens_phrase(num):
    if num < 100:
        return ones[num]



def get_hundreds_phrase(num):
    tens_num = num % 100
    hundreds_digit = num // 100

def get_thousands_phrase(num):
    hundreds_num = num % 1000
    thousands_digit = num // 1000
    thousands_phrase = one[thousands_digit]+'-thousand'

# worked on in class// Matthew will clean up and post to review


