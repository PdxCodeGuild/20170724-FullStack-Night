
def even_or_odd(user_input):
    if user_input / 2 == user_input // 2:
        return 'even'
    else:
        return 'odd'

def main():
    user_input = int(input('What is your number: '))
    answer = even_or_odd(user_input)
    print(answer)


main()
