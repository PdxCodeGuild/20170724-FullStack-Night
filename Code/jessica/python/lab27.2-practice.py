# Write a function that returns True if a number within 10 of 100.
def near_10(a):
    if abs(100 - a) <= 10:
        return True
    else:
        return False


def main():
    a = int(input('Enter a number: '))

    print(near_10(a))

main()
