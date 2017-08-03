# Practice 1    Odd or Even


def compare(a):
    if a % 2 == 1:
        print(str(a) + ' is odd')
    else:
        print(str(a) + ' is even')

def main():
    a = abs(int(input('Choose any number ')))
    print('You chose ' + str(a))
    compare(a)

main()
