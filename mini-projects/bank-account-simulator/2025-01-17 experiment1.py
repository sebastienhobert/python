# class: blueprint for creating objects (instances) that can have attributes and behaviors

# __init__: constructor automatically invoked when an object of class is created

# self.owner: stores the value of the owner parameter in the instance's owner attribute

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

customer1 = BankAccount("Seb", 30000)

print(customer1.owner)
print(customer1.balance)

"""
print:
Seb
30000
"""

