class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
    
    def get_balance(self):
        return f"Balance: ${self.__balance}"

# Encapsulation in action
account = BankAccount("Alice", 1000)
account.deposit(500)
print(account.get_balance())
