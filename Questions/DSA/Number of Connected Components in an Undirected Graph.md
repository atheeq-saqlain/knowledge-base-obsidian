---
slug: dsa-number-of-connected-components-in-an-undirected-graph
questionType: medium
---

# Number of Connected Components in an Undirected Graph

## Statement

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [aᵢ, bᵢ]` indicates that there is an edge between `aᵢ` and `bᵢ` in the graph.

Return the number of connected components in the graph.

## Description

**Example 1:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/d99cd414-340e-4c6f-083b-1f00fdf9eb00/public)

```java
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2
```

**Example 2:**

![](https://imagedelivery.net/CLfkmk9Wzy8_9HRyug4EVA/3f57f075-5114-473a-b198-b6da0da1cd00/public)

```java
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1
```

**Constraints:**

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= aᵢ <= bᵢ < n`
- `aᵢ != bᵢ`
- There are no repeated edges.

## Correct Answer

<!-- Add a reference solution after solving. -->

## Core Concept

[[Union Find]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Identify that this problem is solved with [[Union Find]] | 1 | true | primary |
| Implement the core [[Union Find]] approach correctly on the input | 2 | true | primary |
| Handle edge cases (empty input, single element, or boundary values) | 1 | false | supporting |
| Model the input as a [[Graph]] (adjacency / components) before searching | 1 | true | primary |
