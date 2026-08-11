---
slug: dsa-remove-nth-node-from-end-of-list
questionType: medium
---

# Remove Nth Node From End of List

## Statement

### Remove Nth Node From End of List

Given the `head` of a linked list and an integer `n`, remove the `nth` node from the end of the list and return its head.

## Description

**Example 1:**

```java
Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
```

**Example 2:**

```java
Input: head = [5], n = 1

Output: []
```

**Example 3:**

```java
Input: head = [1,2], n = 2

Output: [2]
```

**Constraints:**

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

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
