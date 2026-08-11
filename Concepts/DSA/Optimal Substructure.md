---
slug: dsa-optimal-substructure
kind: principle
---
# Optimal Substructure

## Definition

A problem has optimal substructure when an optimal solution is composed of optimal solutions to smaller subproblems — the basis for [[Dynamic Programming]] and [[Greedy]] choices. Requires: [[Dynamic Programming]].

## Description

DP stores sub-answers; greedy commits early when a local choice is provably safe. Overlapping subproblems justify memoization.
