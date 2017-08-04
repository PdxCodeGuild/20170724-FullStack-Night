#   Practice 4  Powers of 2

# create a list that multiplies 2 to the previous number to get a list of powers of 2


def power_of_2(n):
    pow2_list = []
    i = 0
    pow2 = 1

    while i < n:       # sets the while loop to repeat until i = 20 (in this case 2^20
        pow2 *= 2       # index 0 = pow2 initialized as 1 x 2 == index 0 is 2
        i += 1          # this increases the index by 1, 1 < 20 = True and will loop back to the beginning for index 2
        pow2_list.append(pow2)

    return pow2_list


def main():
    pow2_list = power_of_2(4)
    print(pow2_list)


main()
