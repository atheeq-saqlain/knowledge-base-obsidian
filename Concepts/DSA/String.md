---
slug: dsa-string
---

## Definition

A finite, **ordered sequence of characters** where each position is identified by a numeric **index**.

## Description

A string stores text as characters in a fixed order from first to last. The first character is usually at index `0`; the last is at index `length - 1`. Length is the number of characters.

| Operation (typical) | Time |
|---------------------|------|
| Read character by index | O(1) |
| Scan all characters | O(n) |
| Compare two strings of length n | O(n) |

**Example:** `"jar"` has length `3`; the character at index `1` is `'a'`.

Appears wherever text is given as input — words, codes, messages — and is often scanned, counted, or compared character by character.

**Common tasks:** length checks, character tallies, slicing, and equality after transforming order or case.
