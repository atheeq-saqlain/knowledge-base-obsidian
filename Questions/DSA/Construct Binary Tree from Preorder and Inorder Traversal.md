---
slug: dsa-construct-binary-tree-from-preorder-and-inorder-traversal
questionType: medium
---

# Construct Binary Tree from Preorder and Inorder Traversal

## Statement

You are given two integer arrays `preorder` and `inorder`.

- `preorder` is the preorder traversal of a binary tree
- `inorder` is the inorder traversal of the same tree
- Both arrays are of the same size and consist of unique values.

Rebuild the binary tree from the preorder and inorder traversals and return its root.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/938c14d3-6669-47ab-924b-a1a08640f200/public)

```java
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]

Output: [1,2,3,null,null,null,4]
```

**Example 2:**

```java
Input: preorder = [1], inorder = [1]

Output: [1]
```

**Constraints:**

- `1 <= inorder.length <= 1000`.
- `inorder.length == preorder.length`
- `-1000 <= preorder[i], inorder[i] <= 1000`

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
