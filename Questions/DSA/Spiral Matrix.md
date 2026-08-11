---
slug: dsa-spiral-matrix
questionType: medium
---

# Spiral Matrix

## Statement

### Spiral Matrix

Return all elements of a matrix in spiral order.

## Description

Given an `m x n` matrix of integers `matrix`, return a list of all elements within the matrix in _spiral order_.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/fe678b92-8606-4e07-ce70-08ec3479aa00/public)

```java
Input: matrix = [[1,2],[3,4]]

Output: [1,2,4,3]
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/8a460616-db14-4ccf-068b-00aa6d398400/public)

```java
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [1,2,3,6,9,8,7,4,5]
```

**Example 3:**

```java
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

**Constraints:**

- `1 <= matrix.length, matrix[i].length <= 10`
- `-100 <= matrix[i][j] <= 100`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Matrix]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Matrix]] | 1 | true | primary |
| Implement the core [[Matrix]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
