#   Lab 14  Pick 6!


import random       # imports the random module so we can use the random.randint function


def pick6():    # function that picks 6 random numbers between below parameters

    any6 = []       # initialized the any6 variable to an empty list
    for i in range(6):  # for loop to run through the below statements until index number of 6 has been assigned
        any_num = random.randint(1, 99)     # calls the random.randint function to pick a number between 1-99 and assigns it to variable any_num
        any6.append(any_num)        # calls the append() function to append the new random any_num to the any6 list.
    return any6                     # returns the any6 list (or any 6 numbers
'''                             # could do while loop below instead of a for loop
while loop

    win6 = []
    i = 0
    while i < 6:
        win_num = random.randint(1, 99)
        win6.append(win_num)
        i += 1
    return win6
'''


def calculate_payout(risky6, winning6): # new function to calculate the payout for each ticket ran thru w/ parameters are the risky6 & winning6 lists
    n_matches = 0       # we start the function at 0 because zero matches have been found until the below for loop is initiated
    for i in range(6):      # for loop goes through each element and determines if the statement below is true
        if risky6[i] == winning6[i]:    # if the index of risky6 and the same index of winning6 is the same, add 1 to matching numbers for this ticket
            n_matches += 1
            #print(n_matches)
    payout = 0      # initialize payout to 0 because user payout has not been calculated.
    if n_matches == 1:      # runs through each if statement, if statement is true than payout = value for single tiket
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
    winning6 = pick6()      # calls out the pick6() function and assigns the return value to winning6 (in this case, a random list of 6 numbers)
    print(winning6)         # prints the the random list of 6 numbers that is assigned the the variable of winning6

    n_tickets = int(input('How many tickets would you like? '))     # calls the input function to collect a value-assigns to n_tickets
    payouts = 0           # must be assign the variable a value- setting to zero because we have not played. (could assign n and include previous games
    for i in range(n_tickets):  # for loop, while i is in the range of the user input 'n_tickets, run for the amount of tickets
        risky6 = pick6()        # calls the pick() function to return a list of 6 numbers for the user and assigns the variable riksy6
        # print(risky6)
        payout = calculate_payout(risky6, winning6) #calls the calculate_payout() function using the two lists and returns the payout for i ticket
        # print('$' + str(payout))
        payouts += payout       # variable 'payouts' adds any payout from the ticket, then repeats this until all tickets have been checked.

    expense = 2 * n_tickets     # cost of $2 multiplied by the user input n_tickets
    print('You spent $' + str(expense) + ' on ' + str(n_tickets))
    print('You won $' + str(payouts))
    total_winnings = payouts - expense
    print('Your total winnings is $' + str(total_winnings))

main()






