import random


class BankAccount:
    def __init__(self, owner, balance, has_overdraft=False):
        self.owner = owner
        self.balance = balance
        self.has_overdraft = has_overdraft
        self.account_no = random.randint(111111111, 999999999)

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.has_overdraft and amount > self.balance:
            return "Insufficient funds"

        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"Account {self.account_no} - Balance: {self.balance:.2f}"


class SavingsAccount(BankAccount):
    def withdraw(self):
        return "No withdrawals permitted"


# Regular BankAccount
account1 = BankAccount("Fatema", 1000)

print(account1)
print(account1.withdraw(500))
print(account1.balance)

print(account1.withdraw(600))
print(account1.balance)


# BankAccount with overdraft
account2 = BankAccount("Ali", 500, True)

print(account2)
print(account2.withdraw(700))
print(account2.balance)


# SavingsAccount
savings = SavingsAccount("Sara", 2000)

print(savings)
print(savings.withdraw())
print(savings.balance)