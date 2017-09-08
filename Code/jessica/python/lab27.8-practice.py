# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
# fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    fibonacci_list = []
    for i in range(n):
        if i == 0:
            fibonacci_list.append(1)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append((fibonacci_list[i - 1]) + (fibonacci_list[i - 2]))

    return fibonacci_list


def main():
    n = int(input('Enter length of fibonacci number list: '))
    print(fibonacci(n))

main()