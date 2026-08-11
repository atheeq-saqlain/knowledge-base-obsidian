---
slug: dsa-longest-increasing-subsequence
questionType: medium
---

# Longest Increasing Subsequence

## Statement

### Longest Increasing Subsequence

Given an integer array `nums`, return the _length_ of the longest strictly _increasing_ subsequence.

## Description

A **subsequence** is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

- For example, `"cat"` is a subsequence of `"crabt"`.

**Example 1:**

```java
Input: nums = [9,1,4,2,3,3,7]

Output: 4
```

Explanation: The longest increasing subsequence is [1,2,3,7], which has a length of 4.

**Example 2:**

```java
Input: nums = [0,3,1,3,2,3]

Output: 4
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `-1000 <= nums[i] <= 1000`

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
