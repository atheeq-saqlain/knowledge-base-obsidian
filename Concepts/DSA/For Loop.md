---
slug: dsa-for-loop
---

## Definition

A **control construct** that executes a block of code repeatedly, once per step in a predetermined range or sequence.

## Description

A for loop runs the same logic on each step without rewriting it. Common forms:

```python
for i in range(n):    # fixed number of iterations
    ...

for item in items:    # one iteration per item
    ...
```

Use when work must be repeated a known or countable number of times — traversing data, accumulating a result, or applying the same update at each step.

**Common mistake:** off-by-one errors (skipping the first or last step). State clearly whether the range is inclusive or exclusive.

<!-- After publishing to Knowledge Tracker: paste the auto-generated slug in frontmatter. -->
