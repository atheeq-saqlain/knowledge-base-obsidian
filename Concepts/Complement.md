---
slug: complement
---

## Definition

The **complement** of a value relative to a goal is the **other value** that, combined with it, satisfies the goal.

## Description

For a target sum, the complement of `x` is `target - x`. Finding a valid pair means: for each value you see, ask whether its complement has already appeared.

**Example:** `nums = [3, 4, 5, 6]`, `target = 7`

| Value seen | Complement (`7 - value`) | Already seen? |
| ---------- | ------------------------ | ------------- |
| 3          | 4                        | no            |
| 4          | 3                        | yes → pair    |

The same idea applies whenever a problem asks for two parts that together meet a fixed requirement — a sum, a difference, or another fixed combination — not only in code.

How you remember past values (hash table, sorted scan, nested loops) is separate; the concept itself is only “what partner would complete this value?”
