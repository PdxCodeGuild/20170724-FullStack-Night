import random                                       # imported from random module

def pick6():                                        # defined function pick6
    nums = []                                       # created an empty list and set it to the variable nums
    for i in range(6):                              # created a for loop in range of 6.
        random_numbers = random.randint(1, 99)      # assigned a random number between 1 and 99 to the variable random_numbers
        nums.append(random_numbers)                 # appended those random numbers to the empty list (nums)
    return nums                                     # returned nums to the function


def calculate_payout(ticket, winning_numbers):      # defined the function calculate_payout with two parameters
    n_matches = 0                                   # created a variable for number of matches and set it to 0
    for i in range(6):
        if winning_numbers[i] == ticket[i]:         # comparing index of w_n to index of t
          n_matches += 1                            # if they are equal add 1 to n_matches
    if n_matches == 1:                              # if statements for number of matches
        return 4                                    # amount "won" is returned to function
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
    return 0                                        # if no matches, return 0.





def main():                                         # defining the main function
    winning_numbers = pick6()                       # setting winning_numbers to the function pick6
    balance = 0                                     # creating variables for balance, expenses and earnings, setting them to 0
    expenses = 0
    earnings = 0
    for i in range(100000):                         # creating a for loop in range of 100000 (to play 100000x)
        ticket = pick6()                            # setting the ticket variable to the pick6 function
        payout = calculate_payout(ticket, winning_numbers)
        expenses += 2                               # adding 2 to the expenses function for each iteration of the loop
        earnings += payout                          # adding the payout to the earnings function for each iteration
        balance -= 2                                # subtracting 2 from balance for each iteration (cost of ticket)
        balance += payout                           # adding payout to balance for each iteration (winnings)
    roi = (earnings - expenses) / expenses          # calculating roi outside of loop







    print('Your ticket: ' + str(ticket) + ' The winning numbers: ' + str(winning_numbers))
    print(roi)
    print(balance)
    print(calculate_payout(ticket, winning_numbers))

main()                                              # calling main function. (Nothing will appear if main function isn't called)
