class BankAccount:
    def __init__(self, balance, account_number, owner):
        self.balance = balance
        self.account_number = account_number
        self.owner = owner

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account number: {self.account_number}, Balance: {self.balance}")

    def transfer(self, amount, account):
        if amount <= self.balance:
            self.balance -= amount
            account.balance += amount
        else:
            print("Insufficient funds.")


class BankCustomer:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                break

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account

    def display_accounts(self):
        print(f"Accounts for {self.name}:")
        for account in self.accounts:
            print(f"Account number: {account.account_number}, Balance: {account.balance}")


# Example usage
account1 = BankAccount(1000, 1234, "John Doe")
account2 = BankAccount(500, 5678, "John Doe")

customer1 = BankCustomer("John Doe", "123 Main St.")
customer1.add_account(account1)
customer1.add_account(account2)

account1.deposit(500)
account1.display_balance()  # Output: Account number: 1234, Balance: 1500

account1.transfer(200, account2)
account1.display_balance()  # Output: Account number: 1234, Balance: 1300
account2.display_balance()  # Output: Account number: 5678, Balance: 700

customer1.display_accounts()
# Output:
# Accounts for John Doe:
# Account number: 1234, Balance: 1300
# Account number: 5678, Balance: 700

customer1.remove_account(5678)
customer1.display_accounts()
# Output:
# Accounts for John Doe:
# Account number: 1234, Balance: 1300