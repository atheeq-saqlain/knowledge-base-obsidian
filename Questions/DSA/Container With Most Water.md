---
slug: dsa-container-with-most-water
questionType: medium
---

# Container With Most Water

## Statement

You are given an integer array `heights` where `heights[i]` represents the height of the ithith bar.

You may choose any two bars to form a container. Return the _maximum_ amount of water a container can store.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/77f004c6-e773-4e63-7b99-a2309303c700/public)

```java
Input: height = [1,7,2,5,4,7,3,6]

Output: 36
```

**Example 2:**

```java
Input: height = [2,2,2]

Output: 4
```

**Constraints:**

- `2 <= height.length <= 1000`
- `0 <= height[i] <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Two Pointers]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Two Pointers]] | 1 | true | primary |
| Implement the core [[Two Pointers]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Move [[Two Pointers]] based on a clear invariant (sorted order, area, etc.) | 1 | true | primary |
