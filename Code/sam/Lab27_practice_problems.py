# Problem 1 write a func that takes two ints, a and b and returns true if one is positive and the other negative


def pos_and_neg(a, b):
    if a > 0 and b < 0:
        return True
    elif a < 0 and b > 0:
        return True
    else:
        return False

print(pos_and_neg(1, -5))


# Problem 2 write a function that returns True if number within 10 and 100

def range_10_100(a):
    if a >= 90 and a <= 110:
        return True
    else:
        return False

print(range_10_100(103))


# Problem 3 Write a function that takes a string, and returns a list of strings, each missing a different character

def missing_char(a):
    string_list = []
    for i in range(len(a)):
        string_list.append(a[:i] + a[i + 1:])
    return string_list


print(missing_char('kitten'))


# Problem 4 write a function that returns number of occurrences of hi in a given string

def count_hi(sentence):
    hi_count = 0
    for i in range(len(sentence)-1):
        if sentence[i] == 'h' and sentence[i + 1] == 'i':
                hi_count += 1
    return hi_count

print(count_hi('hibyehibyehibyehibyehi'))


# Problem 5 write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

# A generic function that counts the occurrences of a word in a sentence.
def count(sentence, word):
    count = 0
    for i in range(len(sentence)-len(word)+1):
        matched = True
        for j in range(len(word)):
            if sentence[i + j] != word[j]:
                matched = False
                break
        if matched:
            count += 1
    return count

print(count('hibyehibyehibyehibyehi', 'hi'))

# A generic function that checks to see if word is at index i of a sentence
def match(sentence, word, i):
    for j in range(len(word)):
        if sentence[i + j] != word[j]:
            return False
    return True

# Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
def catdog(sentence):
    cat = count(sentence, 'cat')
    dog = count(sentence, 'dog')
    if cat == dog:
        return True
    else:
        return False

print(catdog('catdogcatdogcat'))


# Problem 6 Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def even_even(a):
    even = 0
    for i in a:
        if i / 2 == i // 2:
            even += 1

    return even / 2 == even // 2


print(even_even([4, 2, 4]))


# Problem 7 Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.

nums = [[3, 2, 1], [5, 7, 3], [1, 8, 3]]


def combine_all(nums):
    combine = []
    for i in range(len(nums)):
        for j in nums[i]:
            combine.append(j)
    return combine

print(combine_all(nums))


# Problem 8 Write a function that takes n as a parameter, and returns a list containing the first n
def fibonacci(n):
    fib = []
    for i in range(n):
        if i == 0:
            fib.append(1)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i - 1] + fib[i - 2])
    return fib

print(fibonacci(8))









