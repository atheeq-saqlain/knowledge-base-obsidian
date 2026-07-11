---
slug: frequency
---

## Definition

The **frequency** of a value or event is the **count** of how many times it occurs within a set of observations. Test [[Array]]

## Description

If the observations are `3, 1, 3, 2, 3`, the frequency of `3` is `3`, of `1` is `1`, and of `2` is `1`.

Frequencies can be listed, sorted, or compared without any particular data structure — on paper, in a spreadsheet, or in code.

**Example tallies:**

| Value | Frequency |
| ----- | --------- |
| 1     | 1         |
| 2     | 1         |
| 3     | 3         |

Common uses across domains:

- Duplicate detection (any frequency greater than one)
- Most/least common item
- Comparing distributions (e.g. letter counts in two texts)
- Survey or inventory counts

How you compute frequencies (manual tally, sort and sweep, hash table, SQL `GROUP BY`) depends on context; the concept itself is only the count per distinct value or event.
