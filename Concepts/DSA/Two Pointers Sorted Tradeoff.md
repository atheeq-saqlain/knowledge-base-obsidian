---
slug: dsa-two-pointers-sorted-tradeoff
kind: principle
---
# Two Pointers Sorted Tradeoff

## Definition

Opposite-direction two pointers on a sorted sequence trade an O(n log n) sort (when needed) for O(n) pair search instead of O(n²). Requires: [[Two Pointers]].

## Description

Prefer when order can be destroyed or indices after sort can be recovered; avoid when original indices must be preserved without extra maps.
