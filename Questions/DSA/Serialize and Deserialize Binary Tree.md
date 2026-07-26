---
slug: dsa-serialize-and-deserialize-binary-tree
questionType: medium
---

# Serialize and Deserialize Binary Tree

## Statement

Design algorithms to serialize a binary tree to a string and deserialize it back.

## Description

Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/a9dfb17f-70e9-42a3-ba97-33cfd82f6100/public)

```java
Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
```

**Example 2:**

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

[[Binary Tree]]

## Assessment Checklist

| label                                                               | weight | required | role       |
| ------------------------------------------------------------------- | -----: | :------: | ---------- |
| Identify that this problem is solved with [[Binary Tree]]           |      1 |   true   | primary    |
| Implement the core [[Binary Tree]] approach correctly on the input  |      2 |   true   | primary    |
| Handle edge cases (empty input, single element, or boundary values) |      1 |  false   | supporting |
