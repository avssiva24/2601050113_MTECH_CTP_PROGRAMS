# Session 2 – Dynamic Programming

## Aim

To implement the 0/1 Knapsack problem using Dynamic Programming and analyze its time and space complexity.

## Description

Dynamic Programming is a technique used to solve problems by breaking them into smaller overlapping subproblems and storing their results to avoid repeated calculations.

The 0/1 Knapsack problem involves selecting items with given weights and values so that the total weight does not exceed the capacity of the knapsack while maximizing the total value.

Each item can either be selected or not selected.

## Algorithm

1. Read the number of items.
2. Read the weights and values of the items.
3. Read the capacity of the knapsack.
4. Create a DP table.
5. For each item, check whether its weight can fit into the current capacity.
6. If it fits, calculate:

   * Value obtained by including the item.
   * Value obtained by excluding the item.
7. Select the maximum of these two values.
8. If the item does not fit, use the value from the previous row.
9. The final cell contains the maximum possible value.

## Program File

* `knapsack.py` – Implementation of the 0/1 Knapsack problem using Dynamic Programming.

## Sample Input

```text
Enter number of items: 3
Enter weights: 10 20 30
Enter values: 60 100 120
Enter knapsack capacity: 50
```

## Result

```text
Maximum value: 220
```

## Analysis

Let:

* `n` = number of items
* `W` = knapsack capacity

### Time Complexity

```text
O(nW)
```

The program uses two nested loops: one for the items and one for the capacity.

### Space Complexity

```text
O(nW)
```

A two-dimensional DP table is used to store the results.

## Inference

Dynamic Programming avoids repeated calculations by storing previously calculated results. The 0/1 Knapsack problem can be solved efficiently using a DP table with O(nW) time complexity.

