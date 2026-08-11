---
slug: dsa-pair-sum-complement-reduction
kind: principle
---
# Pair-sum Complement Reduction

## Definition

Finding two values that meet a fixed sum reduces to checking whether the complement of the current value was already seen. Requires: [[Complement Lookup]].

## Description

Explains why one pass with a map beats nested loops: past values are memoized so each new value asks a constant-time membership question. Alternatives (sort + two pointers) trade index fidelity and asymptotic constants.
