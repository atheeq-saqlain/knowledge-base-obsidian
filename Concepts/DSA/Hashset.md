---
slug: dsa-hashset
---

## Definition

A collection that stores **unique values** and supports inserting a value and testing whether a value is present, typically in O(1) average time — like a [[Hashmap]] that only tracks keys.

## Description

Each value appears at most once. Membership checks answer “is this value in the set?” without scanning the whole collection.

| Operation | Typical time |
|-----------|--------------|
| Insert value | O(1) avg |
| Test value exists | O(1) avg |
| Remove value | O(1) avg |

**Example (Python):**

```python
seen = set()
seen.add(3)
3 in seen   # True
2 in seen   # False
```

Also called a set or hash set depending on context.

Used for deduplication, fast membership tests, and algorithms that need to ask “have I seen this before?” or “does the neighbor exist?” without nested scans.

**Tradeoff:** extra space for stored values; no inherent order unless a separate ordered structure is used.
