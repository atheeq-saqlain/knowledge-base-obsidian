---
slug: dsa-prefix-product
---

## Definition

A **prefix product** at index `i` is the product of all elements in a sequence from the start up to (or strictly before) `i`. A **suffix product** is the same idea from the end.

## Description

Walking left to right while multiplying builds prefix products; walking right to left builds suffix products. Once both sides are known, the product of everything except `nums[i]` is `(product left of i) × (product right of i)`.

**Example:** `nums = [1, 2, 4, 6]`

| Index | Left product | Right product | Except-self |
| ----- | ------------ | ------------- | ----------- |
| 0 | 1 (empty) | `2×4×6 = 48` | 48 |
| 1 | 1 | `4×6 = 24` | 24 |
| 2 | `1×2 = 2` | 6 | 12 |
| 3 | `1×2×4 = 8` | 1 (empty) | 8 |

Useful when each answer depends on an aggregate of a contiguous side of the array — products, sums, or other running totals — without rescanning the whole array for every index.

Empty sides are treated as the identity for the operation (1 for product, 0 for sum).
