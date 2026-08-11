---
slug: dsa-counting-bits
questionType: medium
---

# Counting Bits

## Statement

### Counting Bits

Given an integer `n`, count the number of `1`'s in the binary representation of every number in the range `[0, n]`.

Return an array `output` where `output[i]` is the number of `1`'s in the binary representation of `i`.

## Description

**Example 1:**

```java
Input: n = 4

Output: [0,1,1,2,1]
```

Explanation:  
0 --> 0  
1 --> 1  
2 --> 10  
3 --> 11  
4 --> 100

**Constraints:**

- `0 <= n <= 1000`

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
