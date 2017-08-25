class ATM:
    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')
        return self.balance

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        return True

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')
        return self.balance

    def calc_interest(self):
        interest = self.balance*0.001
        self.balance += interest
        return self.balance

    def list_transactions(self):
        for i in range(len(self.transactions)):
            print(self.transactions[i])


def main():
    atm = ATM()
    # atm.deposit(5)
    # atm.withdraw(2)
    # atm.list_transactions()
    # print(atm.check_balance())
    while True:
        action = input('What would you like to do (deposit, withdraw, check balance, history)? ')
        if action == 'deposit':
            amount = int(input('How much would you like to deposit? '))
            print(atm.deposit(amount))
        elif action == 'withdraw':
            amount = int(input('How much would you like to withdraw? '))
            print(atm.withdraw(amount))
        elif action == 'check balance':
            print(atm.check_balance())
        elif action == 'history':
            print(atm.list_transactions())
main()
