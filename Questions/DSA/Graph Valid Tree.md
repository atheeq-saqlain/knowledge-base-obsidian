---
slug: dsa-graph-valid-tree
questionType: medium
---

# Graph Valid Tree

## Statement

### Graph Valid Tree

Given `n` nodes labeled from `0` to `n - 1` and a list of **undirected** edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Description

**Example 1:**

```java
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
```

**Example 2:**

```java
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
```

**Note:**

- You can assume that no duplicate edges will appear in edges. Since all edges are `undirected`, `[0, 1]` is the same as `[1, 0]` and thus will not appear together in edges.

**Constraints:**

- `1 <= n <= 100`
- `0 <= edges.length <= n * (n - 1) / 2`

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
