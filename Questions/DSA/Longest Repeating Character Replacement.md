---
slug: dsa-longest-repeating-character-replacement
questionType: medium
---

# Longest Repeating Character Replacement

## Statement

### Longest Repeating Character Replacement

You are given a string `s` consisting of only uppercase english characters and an integer `k`. You can choose up to `k` characters of the string and replace them with any other uppercase English character.

After performing at most `k` replacements, return the length of the longest substring which contains only one distinct character.

## Description

**Example 1:**

```java
Input: s = "XYYX", k = 2

Output: 4
```

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

**Example 2:**

```java
Input: s = "AAABABB", k = 1

Output: 5
```

**Constraints:**

- `1 <= s.length <= 1000`
- `0 <= k <= s.length`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Sliding Window]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Sliding Window]] | 1 | true | primary |
| Implement the core [[Sliding Window]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Maintain window bounds and update a [[Hashmap]] / counts as needed | 1 | true | primary |
