---
slug: dsa-merge-k-sorted-lists
questionType: medium
---

# Merge K Sorted Lists

## Statement

### Merge K Sorted Lists

You are given an array of `k` linked lists `lists`, where each list is sorted in ascending order.

Return the **sorted** linked list that is the result of merging all of the individual linked lists.

## Description

**Example 1:**

```java
Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
```

**Example 2:**

```java
Input: lists = []

Output: []
```

**Example 3:**

```java
Input: lists = [[]]

Output: []
```

**Constraints:**

- `0 <= lists.length <= 1000`
- `0 <= lists[i].length <= 100`
- `-1000 <= lists[i][j] <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Heap]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Heap]] | 1 | true | primary |
| Implement the core [[Heap]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
