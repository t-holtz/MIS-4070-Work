class BankAccount:
    """ Generic bank account. """

    def __init__(self, account_number, account_type, account_name, initial_balance, interest_rate):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = initial_balance
        self.account_type = account_type
        self.interest_rate = interest_rate

    def deposit(self, amount):
        # Complete the code to handle a deposit by adding to the balance.
        self.balance += amount

    def withdraw(self, amount):
        # Complete the code to handle a withdrawal by subtracting from the balance.
        ...
        self.balance -= amount

    def getBalance(self):
        return self.balance

    def getAccountName(self):
        return self.account_name

    def getAccountNumber(self):
        return self.account_number

    def applyInterest(self):
        interest_applied = self.balance * self.interest_rate
        self.balance += interest_applied
        return interest_applied

    def __repr__(self):
        return f"#{self.account_number:4d} {self.account_type:10s} {self.account_name:30s} InterestRate: {self.interest_rate:3.2f} Balance: {self.balance:8.2f}"


class CheckingAccount(BankAccount):
    """ Checking account - no interest. """

    def __init__(self, account_number, account_name, initial_balance):
        BankAccount.__init__(self, account_number, "Checking", account_name, initial_balance, 0)


class SavingsAccount(BankAccount):
    """ Savings account - with interest. """

    def __init__(self, account_number, account_name, initial_balance, interest_rate):
        BankAccount.__init__(self, account_number, "Savings", account_name, initial_balance, interest_rate)


accounts = {
    1000: CheckingAccount(1000, "Main Checking", 1000.0),
    1001: SavingsAccount(1001, "Main Savings", 2000.00, 0.03)
}


def add_account():
    account_number = int(input("Enter new account number: "))
    if account_number in accounts:
        print("Sorry, that account already exists")
        return
    account_name = input("Enter new account name: ")
    account_type = input("Enter account type (Checking or Savings):").capitalize()
    account_balance = float(input("Enter new account initial balance: "))
    if account_type == "Checking":
        new_account = CheckingAccount(account_number, account_name, account_balance)
    elif account_type == "Savings":
        account_rate = float(input("Enter new account interest rate (5% = 0.05): "))
        new_account = SavingsAccount(account_number, account_name, account_balance, account_rate)
    else:
        print(f"Account type {account_type} not recognized")
        return
    accounts[account_number] = new_account


def transaction(choice):
    account_number = int(input("Enter account number: "))
    if account_number not in accounts:
        print("Sorry, that account does not exist")
        return
    account = accounts[account_number]
    if choice == "I":
        amount = account.applyInterest()
        print(f"Applied interest of {amount:.2f} to balance")
    elif choice == "D":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "W":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)


done = False
while not done:
    for account_num, account in accounts.items():
        print(account)
    print("")
    choice = input("Enter (A)dd account, (D)eposit to account, (W)ithdraw, add (I)nterest, or (Q)uit: ").upper()
    if choice == "Q":
        break
    if choice == "A":
        add_account()
    elif choice == "D" or choice == "W" or choice == "I":
        transaction(choice)
    else:
        print(f"Invalid menu choice {choice}")
        continue