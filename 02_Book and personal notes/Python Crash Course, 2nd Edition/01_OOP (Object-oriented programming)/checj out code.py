class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner  # Private attribute
        self.__balance = balance  # Private attribute

    # Getter for owner
    def get_owner(self):
        return self.__owner

    # Setter for owner
    def set_owner(self, owner):
        if isinstance(owner, str):
            self.__owner = owner
        else:
            raise ValueError("Owner name must be a string")

    # Getter for balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Invalid withdrawal amount")

# Create a BankAccount object
account = BankAccount("Alice", 1000)

# Accessing private attributes directly will cause an error
# print(account.__balance)  # AttributeError

# Using getter methods to access private attributes
print(account.get_owner())  # Output: Alice
print(account.get_balance())  # Output: 1000

# Using setter methods to update private attributes
account.set_owner("Bob")
print(account.get_owner())  # Output: Bob

# Depositing money using a public method
account.deposit(500)
print(account.get_balance())  # Output: 1500

# Withdrawing money using a public method
account.withdraw(300)
print(account.get_balance())  # Output: 1200

# Trying to withdraw an invalid amount
try:
    account.withdraw(2000)
except ValueError as e:
    print(e)  # Output: Invalid withdrawal amount
