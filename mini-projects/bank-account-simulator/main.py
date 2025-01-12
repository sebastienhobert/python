class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} depositised. New balance is ${self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} withdrawn. New balance is ${self.balance}")
            else:
                print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")

def main():
    print("Welcome to the Simple Bank Account System")
    owner = input("Enter the account owner's name: ")
    account = BankAccount(owner)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the amount to withdraw "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()