---
slug: dsa-unique-paths
questionType: medium
---

# Unique Paths

## Statement

### Unique Paths

A robot on an `m x n` grid can only move right or down. Return paths from top-left to bottom-right.

## Description

There is an `m x n` grid where you are allowed to move either down or to the right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that can be taken from the top-left corner of the grid (`grid[0][0]`) to the bottom-right corner (`grid[m - 1][n - 1]`).

You may assume the output will fit in a **32-bit** integer.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7eddce4e-2fc4-4c3a-bb0f-9d1060243500/public)

```java
Input: m = 3, n = 6

Output: 21
```

**Example 2:**

```java
Input: m = 3, n = 3

Output: 6
```

**Constraints:**

- `1 <= m, n <= 100`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Dynamic Programming]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Dynamic Programming]] | 1 | true | primary |
| Implement the core [[Dynamic Programming]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Define DP state / transition (or [[Kadane Algorithm]] recurrence) clearly | 1 | true | primary |
