---
slug: dsa-longest-substring-without-repeating-characters
questionType: medium
---

# Longest Substring Without Repeating Characters

## Statement

Given a string `s`, find the _length of the longest substring_ without duplicate characters.

## Description

A **substring** is a contiguous sequence of characters within a string.

**Example 1:**

```java
Input: s = "zxyzxyz"

Output: 3
```

Explanation: The string "xyz" is the longest without duplicate characters.

**Example 2:**

```java
Input: s = "xxxx"

Output: 1
```

**Constraints:**

- `0 <= s.length <= 1000`
- `s` may consist of printable ASCII characters.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Sliding Window]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify [[Sliding Window]] as the approach | 1 | true | primary |
| Expand/shrink while maintaining unique chars (often via [[Hashmap]]) | 2 | true | primary |
| Preserve the [[Window Validity Invariant]] after each bound move | 1 | false | supporting |
