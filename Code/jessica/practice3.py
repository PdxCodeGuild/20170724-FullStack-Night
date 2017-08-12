# 3 write a function that returns the maximum of 3 parameters
def maximum_of_three(a, b, c):
        return max(a, b, c)
print(maximum_of_three(1, 18, -23))


def maximum_of_three(a, b, c):
    if b < c and a < c:
        return c
    elif a < b and b > c:
        return b
    else:
        return a
print(maximum_of_three(23, 17, 2))


#maximum_of_three(5,6,2) will return 6
#maximum_of_three(-4,3,10) will return 10



