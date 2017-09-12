
def opposite(a, b):
    return a < 0 < b or b < 0 < a

# print(opposite(-1, 1))
# print(opposite(1, -1))
# print(opposite(1, 1))
# print(opposite(-1, -1))


def near_100(a):
    # return abs(a-100) < 10
    return 90 <= a <= 110

# print(near_100(99))
# print(near_100(80))
# print(near_100(105))
# print(near_100(140))


def missing_char(s):
    r = []
    for i in range(len(s)):
        t = ''
        for j in range(len(s)):
            if i != j:
                t += s[j]
        r.append(t)
    return r


def missing_char2(s):
    r = []
    for i in range(len(s)):
        r.append(s[:i] + s[i+1:])
    return r


# print(missing_char('kitten'))


def count_hi(sentence):
    c = 0
    for i in range(len(sentence)):
        if sentence[i] == 'h' and i+1 < len(sentence) and sentence[i+1] == 'i':
            c += 1
    return c


def count_hi2(sentence):
    c = 0
    for i in range(len(sentence)-1):
        if sentence[i] == 'h' and sentence[i+1] == 'i':
            c += 1
    return c


# a generic function to return the number of occurances of 'word' in 'sentence'
def count_occurances(sentence, word):
    count = 0
    for i in range(len(sentence)-len(word)+1):
        matched = True
        for j in range(len(word)):
            if sentence[i+j] != word[j]:
                matched = False
                break
        if matched:
            count += 1
    return count


# an accessory function for count_occurances2
# return True if the sentence contains word at index i
def match(sentence, word, i):
    for j in range(len(word)):
        if sentence[i+j] != word[j]:
            return False
    return True


# a second version of count_occurances, using an accessory function
def count_occurances2(sentence, word):
    count = 0
    for i in range(len(sentence)-len(word)+1):
        if match(sentence, word, i):
            count += 1
    return count


# a third version, using the count_occurances function we wrote
def count_hi3(sentence):
    return count_occurances(sentence, 'hi')


# a fourth version, using the count function on string
def count_hi4(sentence):
    return sentence.count('hi')

# print(count_hi('hi'))
# print(count_hi('hihiabchi'))
# print(count_hi('hih'))


def cat_dog(s):
    return s.count('cat') == s.count('dog')


# print(cat_dog('cat'))
# print(cat_dog('catdog'))
# print(cat_dog('catcatdogdog'))


def eveneven(nums):
    n_even = 0
    for num in nums:
        if num%2 == 0:
            n_even += 1
    return n_even%2 == 0

# print(eveneven([2, 2, 2, 3]))
# print(eveneven([2, 2, 2, 3, 2]))


def combine_all(num_lists):
    r = []
    for num_list in num_lists:
        for num in num_list:
            r.append(num)
    return r

#print(combine_all([[5, 2, 3], [4, 5, 1], [7, 6, 3]]))


def fibonacci(n):
    r = []
    for i in range(n):
        if i == 0 or i == 1:
            r.append(1)
        else:
            r.append(r[i-1] + r[i-2])
    return r

# print(fibonacci(8))
