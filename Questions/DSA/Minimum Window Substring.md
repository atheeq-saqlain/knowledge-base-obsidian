---
slug: dsa-minimum-window-substring
questionType: medium
---

# Minimum Window Substring

## Statement

Given two strings `s` and `t`, return the shortest **substring** of `s` such that every character in `t`, including duplicates, is present in the substring. If such a substring does not exist, return an empty string `""`.

You may assume that the correct output is always unique.

## Description

**Example 1:**

```java
Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
```

Explanation: `"YXAZ"` is the shortest substring that includes `"X"`, `"Y"`, and `"Z"` from string `t`.

**Example 2:**

```java
Input: s = "xyz", t = "xyz"

Output: "xyz"
```

**Example 3:**

```java
Input: s = "x", t = "xy"

Output: ""
```

**Constraints:**

- `1 <= s.length <= 1000`
- `1 <= t.length <= 1000`
- `s` and `t` consist of uppercase and lowercase English letters.

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
