# Lab   27  Practice Problems


def opposite(a, b):
    pos_neg = a + b
    if pos_neg == 0:
        pos_neg = 'Undefined'
    elif pos_neg > 0:
        pos_neg = 'True'
    else:
        pos_neg = 'False'
    return pos_neg


def near_100(c):
    if 90 <= c <= 110:
        within_10 = 'True'
    else:
        within_10 = 'False'
    return within_10


def missing_char():
    user_input = input('Type anything here: ')
    missing_char_list = []
    print(user_input)
    for i in range(len(user_input)):
        missing_char_list.append(user_input[:i] + user_input[i+1:])
    return missing_char_list


def count_hi(user_input):
    hi_count = 0
    for i in range(len(user_input)-1):
            if user_input[i] == 'h':
                if user_input[i+1] == 'i':
                    hi_count += 1

    print(hi_count)


def count_word(user_input):
    count = 0
    word = input('What word are you counting? ')
    for i in range(len(user_input)-len(word)+1):
        counting = True
        for j in range(len(word)):
            if user_input[i+j] != word[j]:
                counting = False
                break
        if counting:
            count += 1
    print(count)
    return word, count


def cat_dog():
    user_input = input('Type anything here: ')
    count_1 = count_word(user_input)
    count_2 = count_word(user_input)

    if count_1 == count_2:
        return 'True'
    else:
        return 'False'


def even_even(num_list):
    even_num_count = 0
    for num in num_list:
        if num % 2 == 0:
            even_num_count += 1
    if even_num_count % 2 == 0:
        return 'True'
    else:
       return 'False'


def combine_all(nums):
    print(nums)
    for num in nums:
        print(num)
        for n in num:
            print(n)


def main():
    #print('Are the numbers you input positive or negative?')
    #a = int(input('Type a number: '))
    #b = int(input('Type a second number: '))
    #pos_neg = opposite(a, b)
    #print(pos_neg)

    #print('Is the number you type within 10 of 100?')
    #c = int(input('Type a number: '))

    #within_10 = near_100(c)
    #print(within_10)

    #print('Problem 3')
    #removed_char = missing_char()
    #print(removed_char)

    #print('Problem 4 & 5')
    #counts = cat_dog()
    #print(counts)

    #print('Problem 6')
    #num_list = []
    #entering = True
    #while entering:
    #    user_input = input('Enter a number or type \'done\': ')
    #    if user_input != 'done':
    #        num_list.append(int(user_input))
    #    else:
    #        entering = False
    #even_count = even_even(num_list)
    #print(even_count)

    #print('Problem 6')
    nums = [[5,2,3],[4,5,1],[7,6,3]]
    combine_all(nums)


main()
