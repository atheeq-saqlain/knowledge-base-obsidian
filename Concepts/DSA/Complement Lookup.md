---
slug: complement
kind: schema
---
# Complement Lookup

## Definition

A one-pass technique that, for each value, checks whether its complement relative to a goal was already seen — typically via a [[Hashmap]] over an [[Array]].

## Description

For a target sum, the complement of `x` is `target - x`. Finding a valid pair means: for each value you see, ask whether its complement has already appeared, then store the current value.

**Example:** `nums = [3, 4, 5, 6]`, `target = 7`

| Value seen | Complement (`7 - value`) | Already seen? |
| ---------- | ------------------------ | ------------- |
| 3          | 4                        | no            |
| 4          | 3                        | yes → pair    |

How you remember past values (hash table, sorted scan, nested loops) is separate; the schema is “reduce the pair check to a membership/lookup of the complement.”
