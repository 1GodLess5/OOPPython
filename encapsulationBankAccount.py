class BankAccount:
    def __init__(self, accountNumber, balance):
        self.__accountNumber = accountNumber
        self.__balance = balance

    def getAccountNumber(self):
        return self.__accountNumber

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount

account = BankAccount(123456789, 1000)

print(account.getAccountNumber())
print(account.getBalance())

account.deposit(500)
print(account.getBalance())

account.withdraw(2000)

account.withdraw(25)
print(account.getBalance())