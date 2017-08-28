# 1 write a function that tells whether a number is even or odd (hint, compare a/b and a//b)
def even_or_odd(a):
    if a/2 == a//2:
        print('even')
    else:
        print('odd')
even_or_odd(5)


def even_vs_odd(a):
    if a % 2 == 1:
        print('odd')
    else:
        print('even')
even_vs_odd(6)



