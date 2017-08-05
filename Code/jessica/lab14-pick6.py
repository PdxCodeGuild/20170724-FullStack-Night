import random


def pick6():
    # list building pattern
    ticket = []
    i = 0
    while i < 6:  # more concise to use for i in range
        number = random.randint(1, 99)
        ticket.append(number)
        i += 1
    return ticket
pick6()


def calculate_payoff(ticket, winning):
    n = 0
    for i in range(6):
        if ticket[i] == winning[i]:
            n += 1

    if n == 1:
        return 4
    elif n == 2:
        return 7
    elif n == 3:
        return 100
    elif n == 4:
        return 50000
    elif n == 5:
        return 1000000
    elif n == 6:
        return 25000000
    return 0
# print(calculate_payoff([1, 4, 29, 59, 2, 6], winning) can use this for testing


def main():
    winning = pick6()
    balance = 0
    for i in range(100000):
        ticket = pick6()
        balance = balance - 2 + calculate_payoff(ticket, winning)
    print(balance)

main()







