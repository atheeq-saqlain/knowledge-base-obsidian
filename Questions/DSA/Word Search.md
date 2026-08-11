---
slug: dsa-word-search
questionType: medium
---

# Word Search

## Statement

### Word Search

Given a board and a word, return whether the word exists in the grid via adjacent cells (no reuse).

## Description

Given a 2-D grid of characters `board` and a string `word`, return `true` if the word is present in the grid, otherwise return `false`.

For the word to be present it must be possible to form it with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/7c1fcf82-71c8-4750-3ddd-4ab6a666a500/public)

```java
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "CAT"

Output: true
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/79721392-44b6-4de7-c571-d3d1640ac100/public)

```java
Input: 
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
],
word = "BAT"

Output: false
```

**Constraints:**

- `1 <= board.length, board[i].length <= 5`
- `1 <= word.length <= 10`
- `board` and `word` consists of only lowercase and uppercase English letters.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Backtracking]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Backtracking]] | 1 | true | primary |
| Implement the core [[Backtracking]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
