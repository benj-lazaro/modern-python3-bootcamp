# Create a class called BankAccount
# It has a parameter called owner (string)
# Has an attributed called balance (number); initially assigned with the value of 0.0
# Has a method called deposit(); accepts a number, increments the balance & returns the new balance
# Has a method called withdraw(); accepts a number, decrements the balance & returns the new balance
# Has a method called get_balance(); returns the current balance

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, money_in):
        """deposit(self, number) increments and returns the updated balance."""
        self.balance += money_in
        return self.balance

    def withdraw(self, money_out):
        """withdraw(self, number) decrements and returns the updated balance."""
        self.balance -= money_out
        return self.balance

    def check_balance(self):
        """check_balance(self) returns the current balance."""
        return self.balance


# Instantiate a new object from the class BankAccount
account = BankAccount("Darcy")

# Access instance attribute and methods
print(f"Bank account owner: {account.owner}")
print(f"Current Balance: {account.check_balance()}")

print(f"\nDeposit $10.00...")
print(f"Current Balance: {account.deposit(10)}")

print("\nWithdraw $3.00...")
print(f"Current Balance: {account.withdraw(3)}")
