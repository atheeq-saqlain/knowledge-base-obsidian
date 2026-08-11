---
slug: dsa-valid-parentheses
questionType: medium
---

# Valid Parentheses

## Statement

### Valid Parentheses

Given a string containing only `()[]{}`, return whether the brackets are valid (correctly matched and nested).

## Description

You are given a string `s` consisting of the following characters: `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

**Example 1:**

```java
Input: s = "[]"

Output: true
```

**Example 2:**

```java
Input: s = "([{}])"

Output: true
```

**Example 3:**

```java
Input: s = "[(])"

Output: false
```

Explanation: The brackets are not closed in the correct order.

**Constraints:**

- `1 <= s.length <= 1000`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Stack]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Stack]] | 1 | true | primary |
| Implement the core [[Stack]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
