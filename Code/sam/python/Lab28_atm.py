class Atm:

    def __init__(self, balance=0, interest_rate=0.001,):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')

    def check_withdrawal(self, amount):
        return self.balance >= amount


    def withdraw(self, amount):
        self.balance -= amount

    def calc_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

    def list_transactions(self):
        for transaction in self.transactions:
            print(transaction)









def main():
    atm = Atm()
    while True:
        user_input = input('Please select from the following list:\n\t check balance\n\t deposit\n\t withdraw\n\t calculate interest\n\t list transactions\n\t exit\n\t ')
        if user_input == 'check balance':
            print(f'Your account balance is {atm.check_balance()}')
        elif user_input == 'deposit':
            d_amount = int(input('please input the amount you would like to deposit. '))
            atm.deposit(d_amount)
            print(f'You deposited ${d_amount}. Your new balance is {atm.balance}')
        elif user_input == 'withdraw':
            w_amount = int(input('please input the amount you would like to withdraw. '))
            if atm.check_withdrawal(w_amount):
                atm.withdraw(w_amount)
                print(f'You withdrew {w_amount}. Your new account balance is {atm.balance}. ')

            else:
                print('Invalid funds.')
        elif user_input == 'calculate interest':
            print(f'Your interest rate is {atm.calc_interest()} ')
        elif user_input == 'list transactions':
            atm.list_transactions()
        elif user_input == 'exit':
            break
        else:
            print('Command not valid.')





main()






