# Bank System

# Parent class for Bank Account
class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Ksh. {amount} deposited. New balance: Ksh. {self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Ksh. {amount} withdrawn. New balance: Ksh. {self.balance}"
            return "Insufficient balance."
        return "Withdrawal amount must be positive."

    def get_balance(self):
        return f"Account Balance for {self.account_holder}: KSh.{self.balance}"

    def display_account_info(self):
        return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: Ksh. {self.balance}"


# Creating instances of BankAccount 
account1 = BankAccount("Alice Johnson", "12345678", 500)
account2 = BankAccount("Bob Smith", "87654321", 1000)

# Display account info
print(account1.display_account_info())
print(account2.display_account_info())


print(account1.deposit(200))          
print(account1.withdraw(100))         
print(account1.get_balance())         

print(account2.withdraw(500))         
print(account2.get_balance())         
