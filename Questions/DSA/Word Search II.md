---
slug: dsa-word-search-ii
questionType: medium
---

# Word Search II

## Statement

### Word Search II

Given a board and a word list, return all words that can be formed by adjacent cells (no reuse).

## Description

Given a 2-D grid of characters `board` and a list of strings `words`, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/06435c8e-bac3-49f5-5df7-77fd5dd42800/public)

```java
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/6f244a10-78bf-4a30-0a5f-b8f3e03ce000/public)

```java
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]

Output: []
```

**Constraints:**

- `1 <= board.length, board[i].length <= 12`
- `board[i]` consists only of lowercase English letter.
- `1 <= words.length <= 30,000`
- `1 <= words[i].length <= 10`
- `words[i]` consists only of lowercase English letters.
- All strings within `words` are distinct.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Trie]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Trie]] | 1 | true | primary |
| Implement the core [[Trie]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
