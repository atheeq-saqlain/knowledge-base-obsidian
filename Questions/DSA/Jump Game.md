---
slug: dsa-jump-game
questionType: medium
---

# Jump Game

## Statement

You are given an integer array `nums` where each element `nums[i]` indicates your maximum jump length at that position.

Return `true` if you can reach the last index starting from index `0`, or `false` otherwise.

## Description

**Example 1:**

```java
Input: nums = [1,2,0,1,0]

Output: true
```

Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

**Example 2:**

```java
Input: nums = [1,2,1,0,1]

Output: false
```

**Constraints:**

- `1 <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Greedy]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Greedy]] | 1 | true | primary |
| Implement the core [[Greedy]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
