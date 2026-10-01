# Session 4 – List vs Generator Processing

## Aim

To compare list-based and generator-based processing for a large dataset in terms of execution time and memory usage.

## Description

Python lists store all their elements in memory at the same time.

Generators produce elements one at a time when they are needed. Therefore, generators generally require less memory when processing large datasets.

In this session, both approaches are used to process one million numbers.

## Algorithm

### List Processing

1. Create a list containing one million numbers.
2. Multiply each number by 2.
3. Calculate the sum of the list.
4. Measure the execution time.
5. Measure the memory used by the list.

### Generator Processing

1. Create a generator expression.
2. Generate each number when required.
3. Multiply each number by 2.
4. Calculate the sum.
5. Measure the execution time.
6. Measure the memory used by the generator.

## Program File

* `comparison.py` – Compares list and generator processing.

## Sample Result

The exact execution time depends on the computer and Python environment.

Example:

```text
List sum: 999999000000
Generator sum: 999999000000

List time: <measured time>
Generator time: <measured time>

List memory: <measured memory>
Generator memory: <measured memory>
```

## Analysis

### List

A list stores all generated values in memory.

**Advantages:**

* Easy to access elements.
* Can be reused multiple times.
* Supports indexing.

**Disadvantages:**

* Requires more memory for large datasets.
* All elements are created immediately.

### Generator

A generator produces values one at a time.

**Advantages:**

* Uses much less memory.
* Suitable for large datasets.
* Supports lazy processing.

**Disadvantages:**

* Cannot directly access elements using indexes.
* Once consumed, the generator must be created again for another iteration.

## Complexity

For processing `n` elements:

### List

* Time Complexity: O(n)
* Space Complexity: O(n)

### Generator

* Time Complexity: O(n)
* Additional Space Complexity: O(1)

## Inference

Both list and generator processing can have O(n) time complexity. However, generators are more memory-efficient because they produce values one at a time instead of storing the complete dataset in memory.

