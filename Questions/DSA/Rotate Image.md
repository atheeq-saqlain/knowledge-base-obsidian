---
slug: dsa-rotate-image
questionType: medium
---

# Rotate Image

## Statement

Rotate an `n x n` matrix 90° clockwise in-place.

## Description

Given a square `n x n` matrix of integers `matrix`, rotate it by 90 degrees _clockwise_.

You must rotate the matrix _in-place_. Do not allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/e13e93ed-4fdb-49e4-f971-de1e30356600/public)

```java
Input: matrix = [
  [1,2],
  [3,4]
]

Output: [
  [3,1],
  [4,2]
]
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/37d34844-e6a0-4809-0895-f15e782efe00/public)

```java
Input: matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Output: [
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

**Constraints:**

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

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
