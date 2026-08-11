---
slug: dsa-word-break
questionType: medium
---

# Word Break

## Statement

### Word Break

Return whether `s` can be segmented into a space-separated sequence of dictionary words.

## Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words.

You are allowed to reuse words in the dictionary an unlimited number of times. You may assume all dictionary words are unique.

**Example 1:**

```java
Input: s = "peetcode", wordDict = ["peet","code"]

Output: true
```

Explanation: Return true because "peetcode" can be split into "peet" and "code".

**Example 2:**

```java
Input: s = "applepenapple", wordDict = ["apple","pen","ape"]

Output: true
```

Explanation: Return true because "applepenapple" can be split into "apple", "pen" and "apple". Notice that we can reuse words and also not use all the words.

**Example 3:**

```java
Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]

Output: false
```

**Constraints:**

- `1 <= s.length <= 200`
- `1 <= wordDict.length <= 100`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Dynamic Programming]]

## Assessment Checklist

| label                                                                      | weight | required | role       |
| -------------------------------------------------------------------------- | -----: | :------: | ---------- |
| Identify that this problem is solved with [[Dynamic Programming]]          |      1 |   true   | primary    |
| Implement the core [[Dynamic Programming]] approach correctly on the input |      2 |   true   | primary    |
| Handle edge cases (empty input, single element, or boundary values)        |      1 |  false   | supporting |
| Define DP state / transition (or [[Kadane Algorithm]] recurrence) clearly  |      1 |   true   | primary    |
