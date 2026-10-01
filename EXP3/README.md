# Session 3 – Reusable Python Package: Stack and Queue

## Aim

To implement reusable Stack and Queue data structures in Python using type hints, generics, and dataclasses.

## Description

A Stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle.

A Queue is a linear data structure that follows the **FIFO (First In, First Out)** principle.

In this session, Python dataclasses and type hints are used to create reusable implementations.

## Stack

### Operations

* `push()` – Adds an element to the top of the stack.
* `pop()` – Removes the top element.
* `peek()` – Returns the top element without removing it.

### Algorithm

1. Create an empty stack.
2. Use `push()` to add elements.
3. Use `pop()` to remove the top element.
4. Use `peek()` to view the top element.
5. Display the stack and results.

## Queue

### Operations

* `enqueue()` – Adds an element to the rear of the queue.
* `dequeue()` – Removes an element from the front of the queue.

### Algorithm

1. Create an empty queue.
2. Add elements using `enqueue()`.
3. Remove the first element using `dequeue()`.
4. Display the queue and results.

## Program Files

* `stack.py` – Generic Stack implementation using dataclass.
* `queue.py` – Generic Queue implementation using dataclass and `deque`.

## Sample Result – Stack

```text
Stack: [10, 20, 30]
Popped: 30
Top: 20
```

## Sample Result – Queue

```text
Queue: [10, 20, 30]
Dequeued: 10
Queue after deletion: [20, 30]
```

## Analysis

### Stack

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |

### Queue

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |

Using `deque` allows efficient insertion and deletion from both ends.

## Inference

Stack and Queue are important fundamental data structures. Python generics and type hints make the implementation reusable for different data types, while dataclasses reduce the amount of boilerplate code.

