---
slug: dsa-lowest-common-ancestor-of-a-bst
questionType: medium
---

# Lowest Common Ancestor of a BST

## Statement

### Lowest Common Ancestor of a BST

Given a binary search tree (BST) where all node values are _unique_, and two nodes from the tree `p` and `q`, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes `p` and `q` is the lowest node in a tree `T` such that both `p` and `q` as descendants. The ancestor is allowed to be a descendant of itself.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/2080ee6a-3d27-4cd5-0db2-07672ead8200/public)

```java
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8

Output: 5
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/2080ee6a-3d27-4cd5-0db2-07672ead8200/public)

```java
Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4

Output: 3
```

Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

**Constraints:**

- `2 <= The number of nodes in the tree <= 100`.
- `-100 <= Node.val <= 100`
- `p != q`
- `p` and `q` will both exist in the BST.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Binary Search Tree]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Binary Search Tree]] | 1 | true | primary |
| Implement the core [[Binary Search Tree]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
