---
slug: dsa-merge-two-sorted-lists
questionType: medium
---

# Merge Two Sorted Lists

## Statement

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from `list1` and `list2`.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/51adfea9-493a-4abb-ece7-fbb359d1c800/public)

```java
Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
```

**Example 2:**

```java
Input: list1 = [], list2 = [1,2]

Output: [1,2]
```

**Example 3:**

```java
Input: list1 = [], list2 = []

Output: []
```

**Constraints:**

- `0 <= The length of the each list <= 100`.
- `-100 <= Node.val <= 100`

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
