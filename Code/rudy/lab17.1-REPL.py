#   Practice 2.1    REPL-Read, Evaluate, Test, Loop


def main():
    entering = True
    user_list = []
    while entering:
        x = input('Enter a number ( or \'done\'): ')
        if x == 'done':
            entering = False
        user_list.append(x)

    print(user_list)


main()


