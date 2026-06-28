---
slug:
---

## Definition

A **key–value** collection that supports inserting a pair, retrieving the value for a key, and testing whether a key is present.

## Description

Each key maps to at most one value. Lookup by key is typically O(1) average time in hash-based implementations.

| Operation | Typical time |
|-----------|--------------|
| Insert key → value | O(1) avg |
| Lookup by key | O(1) avg |
| Test key exists | O(1) avg |

**Example (Python):**

```python
counts = {}
counts["a"] = 1
"a" in counts   # True
counts["a"]     # 1
```

Also called dictionary, hash table, map, or associative array depending on context.

Used for deduplication, tallies, caches, indexes, and any task that needs fast “have I seen this before?” or “what is stored under this label?” — in algorithms, databases, and everyday software.

**Tradeoff:** extra space for stored pairs; worst-case slowdown if many keys collide to the same bucket.
