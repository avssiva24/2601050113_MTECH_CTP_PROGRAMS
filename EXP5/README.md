# Experiment 5 – Banking Management System

## Aim

To develop a simple Banking Management System using Object-Oriented Programming, inheritance, abstraction, and type hints.

## Description

Object-Oriented Programming (OOP) is a programming approach where programs are designed using classes and objects.

This program demonstrates:

* Class
* Object
* Inheritance
* Abstraction
* Method overriding
* Type hints

The `BankAccount` class is an abstract base class. The `SavingsAccount` class inherits from it and provides the implementation of the `withdraw()` method.

## Algorithm

1. Create an abstract class named `BankAccount`.
2. Define account number and balance inside the class.
3. Create a `deposit()` method to add money to the balance.
4. Define an abstract `withdraw()` method.
5. Create a `SavingsAccount` class that inherits from `BankAccount`.
6. Implement the `withdraw()` method in `SavingsAccount`.
7. Create a savings account object.
8. Deposit money into the account.
9. Withdraw money from the account.
10. Display the account number and final balance.

## Program File

* `banking.py` – Implements the Banking Management System using OOP.

## Sample Input

The values are directly provided in the program:

```text
Account Number: 101
Initial Balance: 5000
Deposit: 2000
Withdrawal: 1000
```

## Result

```text
Account Number: 101
Balance: 6000
```

## Analysis

### Inheritance

`SavingsAccount` inherits the properties and methods of `BankAccount`.

### Abstraction

`BankAccount` is an abstract class, and `withdraw()` is defined as an abstract method.

### Encapsulation

Account information such as account number and balance is maintained inside the class.

### Type Hints

Type hints are used to specify the expected data types of variables and method parameters.

## Complexity

* Deposit operation: O(1)
* Withdrawal operation: O(1)
* Space Complexity: O(1)

## Inference

The Banking Management System demonstrates how OOP concepts can be used to organize a real-world application. Inheritance allows code reuse, while abstraction defines common behavior for different types of bank accounts.

