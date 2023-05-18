#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient balance. Withdrawal canceled.")

    def check_balance(self):
        return self.account_balance


# Create an instance of the Account class
my_account = Account("123456789", 1000.0, "John Doe")

# Perform transactions
my_account.deposit(500.0)
my_account.withdraw(200.0)
balance = my_account.check_balance()

# Test the program with multiple instances and transactions
account2 = Account("987654321", 2000.0, "Jane Smith")
account2.deposit(1000.0)
account2.withdraw(500.0)
balance2 = account2.check_balance()

print(f"My Account Balance: {balance}")
print(f"Account2 Balance: {balance2}")


# In[ ]:




