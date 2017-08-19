# Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.
def opposite(a, b):
    if a < 0 and b > 0:
        return True
    elif a > 0 and b < 0:
        return True
    else:
        return False


def main():
    a = int(input('Enter a number: '))
    b = int(input('Enter another number: '))

    print(opposite(a, b))

main()