---
slug: dsa-meeting-rooms-ii
questionType: medium
---

# Meeting Rooms II

## Statement

Given an array of meeting time interval objects consisting of start and end times `[[start_1,end_1],[start_2,end_2],...] (start_i < end_i)`, find the minimum number of rooms required to schedule all meetings without any conflicts.

**Note:** `(0,8),(8,10)` is **NOT** considered a conflict at 8.

## Description

**Example 1:**

```java
Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
```

Explanation:  
room1: `(0,40)`  
room2: `(5,10),(15,20)`

**Example 2:**

```java
Input: intervals = [(4,9)]

Output: 1
```

**Constraints:**

- `0 <= intervals.length <= 500`
- `0 <= intervals[i].start < intervals[i].end <= 1,000,000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Heap]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Interval]] | 1 | true | primary |
| Implement the core [[Interval]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
