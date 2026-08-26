---
slug: maths-number-euclid-division-algorithm
kind: schema
---
# Euclid Division Algorithm

## Definition

To find HCF(a, b) with a > b: repeatedly apply the [[Euclid Division Lemma]] a = bq + r (0 ≤ r < b), replacing (a, b) with (b, r) until the remainder is 0. The divisor at that stage is HCF(a, b).

## Description

HCF(a, b) is the largest positive integer that divides both a and b. The process mirrors repeated long division. Example: HCF(4052, 12576) = 4. Applications include stacking equal piles with maximum size and marching two groups in the same maximum number of columns.
