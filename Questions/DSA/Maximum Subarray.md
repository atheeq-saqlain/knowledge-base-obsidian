---
slug: dsa-maximum-subarray
questionType: medium
---

# Maximum Subarray

## Statement

Given an array of integers `nums`, find the subarray with the largest sum and return the sum.

## Description

A **subarray** is a contiguous non-empty sequence of elements within an array.

**Example 1:**

```java
Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
```

Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

**Example 2:**

```java
Input: nums = [-1]

Output: -1
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Kadane Algorithm]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Kadane Algorithm]] | 1 | true | primary |
| Implement the core [[Kadane Algorithm]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Define DP state / transition (or [[Kadane Algorithm]] recurrence) clearly | 1 | true | primary |
