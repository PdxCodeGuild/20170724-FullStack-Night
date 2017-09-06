
# lab 28: ATM


class AtmAccount:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('deposited $' + str(amount))

    def check_withdrawal(self, amount):
        return amount <= self.balance

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append('withdrew $' + str(amount))

    def calc_interest(self):
        self.balance += self.balance * self.interest

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)

atm = AtmAccount()

while True:
    command = input('what would you like to do? (deposit, withdraw, balance, transactions, exit) ')
    if command == 'exit':
        print('goodbye!')
        break
    elif command == 'deposit':
        amount = int(input('how much would you like to deposit? $'))
        atm.deposit(amount)
        print('\tdeposited $' + str(amount))
    elif command == 'withdraw':
        amount = int(input('how much would you like to withdraw? $'))
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)
            print('\twithdrew $' + str(amount))
        else:
            print('you don\'t have that much money in your account')
    elif command == 'balance':
        print('your balance is: $' + str(atm.check_balance()))
    elif command == 'transactions':
        atm.print_transactions()
    else:
        print('command not recognized')





