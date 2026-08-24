---
slug: maths-euclid-division-algorithm
kind: schema
---
# Euclid Division Algorithm

## Definition

To find HCF(a, b) with a > b, repeatedly apply Euclid's division lemma a = bq + r (0 ≤ r < b), replacing (a, b) with (b, r) until r = 0; the last non-zero divisor is HCF(a, b).

## Description

Based on the lemma: given positive integers a and b, there exist whole numbers q and r with a = bq + r, 0 ≤ r < b. Example: HCF(135, 225) = 45.

Applications include marching columns problem (HCF of group sizes).
