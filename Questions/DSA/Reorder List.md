---
slug: dsa-reorder-list
questionType: medium
---

# Reorder List

## Statement

Reorder list `L0→L1→…→Ln` into `L0→Ln→L1→Ln-1→…` in-place.

## Description

You are given the head of a singly linked-list.

The positions of a linked list of `length = 7` for example, can intially be represented as:

`[0, 1, 2, 3, 4, 5, 6]`

Reorder the nodes of the linked list to be in the following order:

`[0, 6, 1, 5, 2, 4, 3]`

Notice that in the general case for a list of `length = n` the nodes are reordered to be in the following order:

`[0, n-1, 1, n-2, 2, n-3, ...]`

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

**Example 1:**

```java
Input: head = [2,4,6,8]

Output: [2,8,4,6]
```

**Example 2:**

```java
Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
```

**Constraints:**

- `1 <= Length of the list <= 1000`.
- `1 <= Node.val <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Linked List]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Linked List]] | 1 | true | primary |
| Implement the core [[Linked List]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
