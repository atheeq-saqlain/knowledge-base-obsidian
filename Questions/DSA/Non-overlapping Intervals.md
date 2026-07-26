---
slug: dsa-non-overlapping-intervals
questionType: medium
---

# Non-overlapping Intervals

## Statement

Given an array of intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note: Intervals are _non-overlapping_ even if they have a common point. For example, `[1, 3]` and `[2, 4]` are overlapping, but `[1, 2]` and `[2, 3]` are non-overlapping.

## Description

**Example 1:**

```java
Input: intervals = [[1,2],[2,4],[1,4]]

Output: 1
```

Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

**Example 2:**

```java
Input: intervals = [[1,2],[2,4]]

Output: 0
```

**Constraints:**

- `1 <= intervals.length <= 1000`
- `intervals[i].length == 2`
- `-50000 <= starti < endi <= 50000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Interval]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Interval]] | 1 | true | primary |
| Implement the core [[Interval]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
