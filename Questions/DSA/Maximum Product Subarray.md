---
slug: dsa-maximum-product-subarray
questionType: medium
---

# Maximum Product Subarray

## Statement

### Maximum Product Subarray

Given an integer array `nums`, find a **subarray** that has the largest product, and return the product.

## Description

A **subarray** is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a **32-bit** integer.

**Note** that the product of an array with a single element is the value of that element.

**Example 1:**

```java
Input: nums = [2,4,-3,5]

Output: 8
```

Explanation: `[2,4]` has the largest product `8`.

  

**Example 2:**

```java
Input: nums = [-3,0,-2]

Output: 0
```

Explanation: The result cannot be `6`, because `[-3,-2]` is not a subarray.

  

**Constraints:**

- `1 <= nums.length <= 1000`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is **guaranteed** to fit in a **32-bit** integer.

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
