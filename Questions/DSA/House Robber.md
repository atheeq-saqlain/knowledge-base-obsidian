---
slug: dsa-house-robber
questionType: medium
---

# House Robber

## Statement

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a straight line, i.e. the `i`th house is the neighbor of the `(i-1)`th and `(i+1)`th house.

You are planning to rob money from the houses, but you cannot rob **two adjacent houses** because the security system will automatically alert the police if two adjacent houses were _both_ broken into.

Return the _maximum_ amount of money you can rob **without** alerting the police.

## Description

**Example 1:**

```java
Input: nums = [1,1,3,3]

Output: 4
```

Explanation: `nums[0] + nums[2] = 1 + 3 = 4`.

**Example 2:**

```java
Input: nums = [2,9,8,3,6]

Output: 16
```

Explanation: `nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16`.

**Constraints:**

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100` 

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Dynamic Programming]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Dynamic Programming]] | 1 | true | primary |
| Implement the core [[Dynamic Programming]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Define DP state / transition (or [[Kadane Algorithm]] recurrence) clearly | 1 | true | primary |
