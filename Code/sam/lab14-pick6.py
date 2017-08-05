import random


def pick6():
    nums = []
    for i in range(6):
        random_numbers = random.randint(1, 99)
        nums.append(random_numbers)
    return nums


def calculate_payout(ticket, winning_numbers):
    n_matches = 0
    for i in range(6):
        if winning_numbers[i] == ticket[i]:
          n_matches += 1
    if n_matches == 1:
        return 4
    elif n_matches == 2:
        return 7
    elif n_matches == 3:
        return 100
    elif n_matches == 4:
        return 50000
    elif n_matches == 5:
        return 1000000
    elif n_matches == 6:
        return 25000000
    return 0





def main():
    winning_numbers = pick6()
    balance = 0
    expenses = 0
    earnings = 0
    for i in range(100000):
        ticket = pick6()
        payout = calculate_payout(ticket, winning_numbers)
        expenses += 2
        earnings += payout
        balance -= 2
        balance += payout
    roi = (earnings - expenses) / expenses







    print('Your ticket: ' + str(ticket) + ' The winning numbers: ' + str(winning_numbers))
    print(roi)
    print(balance)
    print(calculate_payout(ticket, winning_numbers))

main()
