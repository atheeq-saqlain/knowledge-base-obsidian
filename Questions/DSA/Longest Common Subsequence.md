---
slug: dsa-longest-common-subsequence
questionType: medium
---

# Longest Common Subsequence

## Statement

### Longest Common Subsequence

Given two strings `text1` and `text2`, return the length of the _longest common subsequence_ between the two strings if one exists, otherwise return `0`.

## Description

A **subsequence** is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

- For example, `"cat"` is a subsequence of `"crabt"`.

A **common subsequence** of two strings is a subsequence that exists in both strings.

**Example 1:**

```java
Input: text1 = "cat", text2 = "crabt" 

Output: 3 
```

Explanation: The longest common subsequence is "cat" which has a length of 3.

**Example 2:**

```java
Input: text1 = "abcd", text2 = "abcd"

Output: 4
```

**Example 3:**

```java
Input: text1 = "abcd", text2 = "efgh"

Output: 0
```

**Constraints:**

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

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
