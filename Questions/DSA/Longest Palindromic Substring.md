---
slug: dsa-longest-palindromic-substring
questionType: medium
---

# Longest Palindromic Substring

## Statement

### Longest Palindromic Substring

Given a string `s`, return the longest substring of `s` that is a [[Palindrome]].

## Description

A **palindrome** is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

**Example 1:**

```java
Input: s = "ababd"

Output: "bab"
```

Explanation: Both "aba" and "bab" are valid answers.

**Example 2:**

```java
Input: s = "abbc"

Output: "bb"
```

**Constraints:**

- `1 <= s.length <= 1000`
- `s` contains only digits and English letters.

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
