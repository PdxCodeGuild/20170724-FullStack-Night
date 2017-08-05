#   Lab 14  Pick 6!


import random


def pick6():

    win6 = []
    for i in range(6):
        win_num = random.randint(1, 99)
        win6.append(win_num)
    return win6
'''
while loop

    win6 = []
    i = 0
    while i < 6:
        win_num = random.randint(1, 99)
        win6.append(win_num)
        i += 1
    return win6
'''


def calculate_payout(risky6, winning6):
    n_matches = 0
    for i in range(6):
        if risky6[i] == winning6[i]:
            n_matches += 1
            #print(n_matches)
    payout = 0
    if n_matches == 1:
        payout += 4
    elif n_matches == 2:
        payout += 7
    elif n_matches == 3:
        payout += 100
    elif n_matches == 4:
        payout += 50000
    elif n_matches == 5:
        payout += 1000000
    elif n_matches == 6:
        payout += 25000000
    return payout

    # if 1 number matches, you win $4
    # if 2 numbers match, you win $7
    # if 3 numbers match, you win $100
    # if 4 numbers match, you win $50, 000
    # if 5 numbers match, you win  # 1,000,000
    # if 6 numbers match, you win  # 25,000,000


def main():
    winning6 = pick6()
    print(winning6)

    n_tickets = int(input('How many tickets would you like? '))
    payouts = 0
    for i in range(n_tickets):
        risky6 = pick6()
        # print(risky6)
        payout = calculate_payout(risky6, winning6)
        # print('$' + str(payout))
        payouts += payout

    expense = 2 * n_tickets
    print('You spent $' + str(expense) + ' on ' + str(n_tickets))
    earnings = payouts
    print('You won $' + str(earnings))
    total_winnings = earnings - expense
    print('Your total winnings is $' + str(total_winnings))

main()






