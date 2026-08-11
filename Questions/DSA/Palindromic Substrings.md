---
slug: dsa-palindromic-substrings
questionType: medium
---

# Palindromic Substrings

## Statement

### Palindromic Substrings

Given a string `s`, return the number of substrings within `s` that are palindromes.

## Description

A **palindrome** is a string that reads the same forward and backward.

**Example 1:**

```java
Input: s = "abc"

Output: 3
```

Explanation: "a", "b", "c".

**Example 2:**

```java
Input: s = "aaa"

Output: 6
```

Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

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
