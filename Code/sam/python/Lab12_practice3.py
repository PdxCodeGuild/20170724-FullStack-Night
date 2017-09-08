

def maximum_of_three(a, b, c):              # defining function with three parameters
    if a < b:
        if b < c:                           # nesting if statement, comparing b and c
            return c                        # returning c if larger than b
        else:
            return b                        # returning b if larger than c
    else:
        if a > c:                           # comparing a and c
            return a                        # returning a if larger than c
        else:
            return c                        # returning c if larger than a


maximum_number = maximum_of_three(3, 4, 5)
print(maximum_number)




