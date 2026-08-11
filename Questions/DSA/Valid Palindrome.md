---
slug: dsa-valid-palindrome
questionType: medium
---

# Valid Palindrome

## Statement

### Valid Palindrome

Given a string `s`, return `true` if it is a palindrome after converting to lowercase and removing non-alphanumeric characters.

## Description

Given a string `s`, return `true` if it is a **palindrome**, otherwise return `false`.

A **palindrome** is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

**Note:** Alphanumeric characters consist of letters `(A-Z, a-z)` and numbers `(0-9)`.

**Example 1:**

```java
Input: s = "Was it a car or a cat I saw?"

Output: true
```

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

**Example 2:**

```java
Input: s = "tab a cat"

Output: false
```

Explanation: "tabacat" is not a palindrome.

**Constraints:**

- `1 <= s.length <= 1000`
- `s` is made up of only printable ASCII characters.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Two Pointers]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Two Pointers]] | 1 | true | primary |
| Implement the core [[Two Pointers]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Move [[Two Pointers]] based on a clear invariant (sorted order, area, etc.) | 1 | true | primary |
