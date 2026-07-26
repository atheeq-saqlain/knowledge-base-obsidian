---
slug: dsa-best-time-to-buy-and-sell-stock
questionType: medium
---

# Best Time to Buy and Sell Stock

## Statement

You are given an integer array `prices` where `prices[i]` is the price of Coin on the `ith` day.

You may choose a **single day** to buy one Coin and choose a **different day in the future** to sell it.

Return the maximum profit you can achieve. You may choose to **not make any transactions**, in which case the profit would be `0`.

## Description

**Example 1:**

```java
Input: prices = [10,1,5,6,7,1]

Output: 6
```

Explanation: Buy `prices[1]` and sell `prices[4]`, `profit = 7 - 1 = 6`.

**Example 2:**

```java
Input: prices = [10,8,7,5,2]

Output: 0
```

Explanation: No profitable transactions can be made, thus the max profit is 0.

**Constraints:**

- `1 <= prices.length <= 100`
- `0 <= prices[i] <= 100`

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Sliding Window]]

## Assessment Checklist

| label                                                                 | weight | required | role       |
| --------------------------------------------------------------------- | -----: | :------: | ---------- |
| Identify that this problem is solved with [[Sliding Window]]          |      1 |   true   | primary    |
| Implement the core [[Sliding Window]] approach correctly on the input |      2 |   true   | primary    |
| Handle edge cases (empty input, single element, or boundary values)   |      1 |  false   | supporting |
| Maintain window bounds and update a [[Hashmap]] / counts as needed    |      1 |   true   | primary    |
