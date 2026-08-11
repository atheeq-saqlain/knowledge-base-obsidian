---
slug: dsa-window-validity-invariant
kind: principle
---
# Window Validity Invariant

## Definition

A sliding window stays correct when every expand/shrink restores the problem constraint (validity invariant) before recording an answer. Requires: [[Sliding Window]].

## Description

If the constraint is not about a contiguous range, or validity is not monotonic with bound moves, sliding window does not apply.
