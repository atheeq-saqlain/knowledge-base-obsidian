---
slug: dsa-group-anagrams
questionType:
---

# Group Anagrams

## Statement

### Group Anagrams

Given an array of strings `strs`, group all anagrams together into sublists. You may return the output in any order.

## Description

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

```java
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

**Example 2:**

```java
Input: strs = ["x"]

Output: [["x"]]
```

**Example 3:**

```java
Input: strs = [""]

Output: [[""]]
```

## Correct Answer

```Python
class Solution:

    def groupAnagrams(self, strs):
        dic = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key not in dic:
                dic[key] = []
            dic[key].append(s)
        return list(dic.values())


sol = Solution()
res = sol.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"])
print(res)
```

## Core Concept

[[Hashmap]]

## Assessment Checklist

| label                                                                                         | weight | required | role    |
| --------------------------------------------------------------------------------------------- | -----: | :------: | ------- |
| Build a character [[Frequency]] signature for each [[String]]                                 |      1 |   true   | primary |
| Use a [[Hashmap]] to group [[String]]s that share the same [[Frequency]] signature            |      1 |   true   | primary |
| Use a [[For Loop]] to process each [[String]] in the [[Array]]                                |      1 |   true   | primary |
| Return the grouped sublists from the [[Hashmap]] values                                       |      1 |   true   |         |
