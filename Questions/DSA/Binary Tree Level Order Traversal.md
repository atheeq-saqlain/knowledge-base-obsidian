---
slug: dsa-binary-tree-level-order-traversal
questionType: medium
---

# Binary Tree Level Order Traversal

## Statement

### Binary Tree Level Order Traversal

Given a binary tree `root`, return the level order traversal of it as a nested list, where each sublist contains the values of nodes at a particular level in the tree, from left to right.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/a4639809-0754-4eda-221f-a4cd58bd9c00/public)

```java
Input: root = [1,2,3,4,5,6,7]

Output: [[1],[2,3],[4,5,6,7]]
```

**Example 2:**

```java
Input: root = [1]

Output: [[1]]
```

**Example 3:**

```java
Input: root = []

Output: []
```

**Constraints:**

- `0 <= The number of nodes in the tree <= 1000`.
- `-1000 <= Node.val <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Breadth First Search]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Breadth First Search]] | 1 | true | primary |
| Implement the core [[Breadth First Search]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
