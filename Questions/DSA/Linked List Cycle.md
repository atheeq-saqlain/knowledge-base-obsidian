---
slug: dsa-linked-list-cycle
questionType: medium
---

# Linked List Cycle

## Statement

### Linked List Cycle

Given the beginning of a linked list `head`, return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Description

There is a cycle in a linked list if at least one node in the list can be visited again by following the `next` pointer.

Internally, `index` determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's `next` pointer to the `index-th` node. If `index = -1`, then the tail node points to `null` and no cycle exists.

**Note:** `index` is **not** given to you as a parameter.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/3ecdbcfc-70fc-429a-4654-cf4f6a7dbe00/public)

```java
Input: head = [1,2,3,4], index = 1

Output: true
```

Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/89e6716c-9f65-46da-d7b2-f04a93269700/public)

```java
Input: head = [1,2], index = -1

Output: false
```

**Constraints:**

- `0 <= Length of the list <= 1000`.
- `-1000 <= Node.val <= 1000`
- `index` is `-1` or a valid index in the linked list.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Two Pointers]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Linked List]] | 1 | true | primary |
| Implement the core [[Linked List]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
