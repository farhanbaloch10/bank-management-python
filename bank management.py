import datetime
import hashlib

class Transaction:
    def __init__(self, amount, type, timestamp):
        self.amount = amount
        self.type = type
        self.timestamp = timestamp

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transactions.append(Transaction(amount, 'Deposit', datetime.datetime.now()))
            return True
        else:
            raise ValueError("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(Transaction(amount, 'Withdrawal', datetime.datetime.now()))
            return True
        else:
            raise ValueError("Insufficient funds or invalid withdrawal amount")

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def apply_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(Transaction(interest, 'Interest', datetime.datetime.now()))

class Bank:
    def __init__(self, name):
        self.__name = name
        self.__accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number not in self.__accounts:
            self.__accounts[account_number] = BankAccount(account_number, account_holder, initial_balance)
            return True
        else:
            raise ValueError("Account already exists")

    def get_account(self, account_number):
        return self.__accounts.get(account_number)

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
        raise ValueError("Transfer failed")

def main():
    bank = Bank("Secure Bank")
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer")
        print("6. Apply Interest")
        print("7. Transaction History")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            try:
                bank.create_account(account_number, account_holder, initial_balance)
                print("Account created successfully!")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                try:
                    account.deposit(amount)
                    print("Deposit successful!")
                except ValueError as e:
                    print(str(e))
            else:
                print("Account not found!")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                try:
                    account.withdraw(amount)
                    print("Withdrawal successful!")
                except ValueError as e:
                    print(str(e))
            else:
