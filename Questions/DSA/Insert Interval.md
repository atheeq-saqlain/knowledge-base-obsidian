---
slug: dsa-insert-interval
questionType: medium
---

# Insert Interval

## Statement

### Insert Interval

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represents the start and the end time of the `ith` interval. `intervals` is initially sorted in ascending order by `start_i`.

You are given another interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and also `intervals` still does not have any overlapping intervals. You may merge the overlapping intervals if needed.

Return `intervals` after adding `newInterval`.

Note: Intervals are _non-overlapping_ if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

## Description

**Example 1:**

```java
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]

Output: [[1,6]]
```

Explanation: `[2,5]` overlaps with `[1,3]` and `[4,6]`, so all three are merged into `[1,6]`.

**Example 2:**

```java
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]

Output: [[1,2],[3,5],[6,7],[9,10]]
```

Explanation: `[6,7]` does not overlap with any existing interval, so it is simply inserted between `[3,5]` and `[9,10]`.

**Constraints:**

- `0 <= intervals.length <= 1000`
- `newInterval.length == intervals[i].length == 2`
- `0 <= start <= end <= 1000`

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
