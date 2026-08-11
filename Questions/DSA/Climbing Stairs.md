---
slug: dsa-climbing-stairs
questionType: medium
---

# Climbing Stairs

## Statement

### Climbing Stairs

You are given an integer `n` representing the number of steps to reach the top of a staircase. You can climb with either `1` or `2` steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

## Description

**Example 1:**

```java
Input: n = 2

Output: 2
```

Explanation:

1. `1 + 1 = 2`
2. `2 = 2`

**Example 2:**

```java
Input: n = 3

Output: 3
```

Explanation:

1. `1 + 1 + 1 = 3`
2. `1 + 2 = 3`
3. `2 + 1 = 3`

**Constraints:**

- `1 <= n <= 45`

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
