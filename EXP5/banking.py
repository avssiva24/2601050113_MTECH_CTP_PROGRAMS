from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number: int, balance: float):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(BankAccount):
    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")


account = SavingsAccount(101, 5000)

account.deposit(2000)
account.withdraw(1000)

print("Account Number:", account.account_number)
print("Balance:", account.balance)
