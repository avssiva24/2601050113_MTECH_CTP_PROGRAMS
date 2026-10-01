# Experiment 6 – Dataclass and Traditional Class

## Aim

To create a Student data model using a traditional Python class and a dataclass, and compare their implementation.

## Description

A Python class can be used to represent an object containing data and behavior.

A `dataclass` is a Python feature that makes it easier to create classes mainly used for storing data. It automatically provides useful methods such as `__init__()` and `__repr__()`.

In this experiment, the same Student information is represented using:

1. Traditional class
2. Dataclass

## Algorithm

1. Create a traditional `Student` class.
2. Define the `__init__()` method.
3. Create a `StudentData` class using `@dataclass`.
4. Define `name` and `roll_no` as fields.
5. Create an object using the traditional class.
6. Create another object using the dataclass.
7. Display the values of both objects.
8. Compare the implementations.

## Program File

* `student.py` – Compares a traditional class with a dataclass.

## Sample Data

```text
Name: Ravi
Roll No: 101
```

## Result

```text
Traditional class:
Name: Ravi
Roll No: 101

Dataclass:
StudentData(name='Ravi', roll_no=101)
```

## Comparison

| Feature                  | Traditional Class        | Dataclass               |
| ------------------------ | ------------------------ | ----------------------- |
| `__init__()`             | Written manually         | Automatically generated |
| `__repr__()`             | Usually written manually | Automatically generated |
| Code length              | More                     | Less                    |
| Suitable for data models | Yes                      | Yes                     |
| Type hints               | Can be used              | Commonly used           |

## Analysis

The traditional class requires the programmer to write the constructor manually.

The dataclass automatically generates the constructor and other useful methods, which reduces the amount of code required.

For classes mainly used to store data, dataclasses can make the code simpler and easier to maintain.

## Complexity

Creating either object takes:

* Time Complexity: O(1)
* Space Complexity: O(1)

## Inference

Dataclasses provide a simple and convenient way to create data models in Python. They reduce boilerplate code while keeping the class readable and type-friendly. Traditional classes are still useful when more customized behavior is required.

