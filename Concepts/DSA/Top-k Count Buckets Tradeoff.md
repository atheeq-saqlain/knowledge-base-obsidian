---
slug: dsa-top-k-count-buckets-tradeoff
kind: principle
---
# Top-k Count Buckets Tradeoff

## Definition

After counting frequencies, top-k can be taken via sort, heap, or buckets indexed by count — buckets are O(n) when counts are bounded by n. Requires: [[Frequency Count]], [[Bucket by Frequency]].

## Description

Choose buckets when frequency range is small; heap/sort when k is tiny or counts are huge.
