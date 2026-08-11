---
slug: dsa-reverse-bits
questionType: medium
---

# Reverse Bits

## Statement

### Reverse Bits

Reverse the bits of a 32-bit unsigned integer.

## Description

Given a 32-bit unsigned integer `n`, reverse the bits of the binary representation of `n` and return the result.

**Example 1:**

```java
Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
```

Explanation: Reversing `00000000000000000000000000010101`, which represents the unsigned integer `21`, gives us `10101000000000000000000000000000` which represents the unsigned integer `2818572288`.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Bit Manipulation]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Bit Manipulation]] | 1 | true | primary |
| Implement the core [[Bit Manipulation]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
