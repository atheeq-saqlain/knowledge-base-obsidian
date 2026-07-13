---
slug: dsa-bucket-sort
---

## Definition

A sorting approach that places each element into a **bucket** indexed by a key (often an integer), then collects the buckets in key order.

## Description

Instead of comparing elements to each other, you use the key as an index into an array of buckets. Elements with the same key land in the same bucket. Reading the buckets from low key to high (or the reverse) yields a sorted order.

**Example:** values with frequencies `1 → 1`, `2 → 2`, `3 → 3` can be placed into buckets indexed by frequency:

| Bucket index (frequency) | Values |
| ------------------------ | ------ |
| 1                        | 1      |
| 2                        | 2      |
| 3                        | 3      |

Scanning from the highest index downward visits values from most frequent to least frequent.

Useful when keys are integers in a known, limited range — for example ranking by count, digit, or age bracket. Tradeoff: needs space for every possible key index, including empty buckets.
