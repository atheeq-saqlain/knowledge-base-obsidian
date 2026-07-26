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
| Identify that this problem is solved with [[Sliding Window]] | 1 | true | primary |
| Implement the core [[Sliding Window]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Maintain window bounds and update a [[Hashmap]] / counts as needed | 1 | true | primary |
