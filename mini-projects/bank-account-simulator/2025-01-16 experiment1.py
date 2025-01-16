class BankAccount:
    def __init__(self, owner, balance=0): # __init__ is a constructor
        self.owner = owner # self refers to the instance of the class being created
        self.balance = balance

account1 = BankAccount("Alice", 100) # self.owner = "Alice" for account1
account2 = BankAccount("Bob") # self.owner = "Bob" for account2

print(account1.owner)
print(account1.balance)

print(account2.owner)
print(account2.balance)

