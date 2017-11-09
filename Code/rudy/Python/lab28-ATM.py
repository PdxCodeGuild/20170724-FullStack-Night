#   Lab 28  ATM


class ATM:
    def __init__(self, balance=0, interest_rate=1/1000):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')

    def check_withdrawal(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')

    def calc_interest(self):
        self.balance += self.balance*self.interest_rate

    def list_transactions(self):
        for transaction in self.transactions:
            print(transaction)


def atm_action():
    print('1.Deposit\n2.Withdraw\n3.Calculate Interest')
    action = input('Enter the # you would like to perform? ')
    if action == '1':
        action = 'Deposit'
        amount = float(input(f'How much would you like to {action}? '))
        return amount, action
    elif action == '2':
        action = 'Withdraw'
        amount = float(input(f'How much would you like to {action}? '))
        return amount, action
    elif action == '3':
        action = 'Calculate Interest on'
        return 0, action


def main():
    atm = ATM()
    while True:
        amount, action = atm_action()

        if action == 'Deposit':
            atm.deposit(amount)

        elif action == "Withdraw":
            if atm.check_withdrawal(amount):
                atm.withdraw(amount)
            else:
                print('Insufficient Funds')
        elif action == 'Calculate Interest on':
            atm.calc_interest()
        print('%.2f' % atm.check_balance())
        atm.list_transactions()

        complete = input('Would you like to make another transaction? ').lower()
        if complete == ['y', 'yes', 'yeah']:
            complete = 'y'
        elif complete == ['n', 'no', 'nah', 'nope']:
            complete = 'n'

        if complete == 'n':
            break


main()
