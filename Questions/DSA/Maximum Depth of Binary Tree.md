---
slug: dsa-maximum-depth-of-binary-tree
questionType: medium
---

# Maximum Depth of Binary Tree

## Statement

Return the maximum depth of a binary tree.

## Description

The **depth** of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/5ea6da77-7e43-43e0-dd9d-e879ca0b1600/public)

```java
Input: root = [1,2,3,null,null,4]

Output: 3
```

**Example 2:**

```java
Input: root = []

Output: 0
```

**Constraints:**

- `0 <= The number of nodes in the tree <= 100`.
- `-100 <= Node.val <= 100`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Depth First Search]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Binary Tree]] | 1 | true | primary |
| Implement the core [[Binary Tree]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
