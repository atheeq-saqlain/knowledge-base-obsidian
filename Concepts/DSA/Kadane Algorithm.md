---
slug: dsa-kadane-algorithm
kind: schema
---

# Kadane Algorithm

## Definition

A linear scan that tracks the best subarray sum ending at the current index to find the maximum subarray sum. Requires: [[Array]], [[Dynamic Programming]].

## Description

Classic greedy/DP hybrid: at each step, either extend the previous subarray or start a new one.
