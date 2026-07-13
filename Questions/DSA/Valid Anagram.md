---
slug: dsa-valid-anagram
questionType:
---

# Valid Anagram

## Statement

### Valid Anagram

Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, otherwise return `false`.

## Description

An **anagram** is a string that contains the exact same characters as another string, but the order of the characters can be different.

**Example 1:**

```java
Input: s = "racecar", t = "carrace"

Output: true
```

**Example 2:**

```java
Input: s = "jar", t = "jam"

Output: false
```

**Constraints:**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Correct Answer

```Python
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1

        for c in t:
            if c not in dic or dic[c] == 0:
                return False
            dic[c] -= 1

        return True


sol = Solution()
res = sol.isAnagram("racecar", "carrace")
print(res)
```

## Core Concept

[[Frequency]]

## Assessment Checklist

| label                                                                                      | weight | required | role       |
| ------------------------------------------------------------------------------------------ | -----: | :------: | ---------- |
| Return false early when the two [[String]]s have different lengths                         |      1 |   true   | supporting |
| Use a [[Hashmap]] to store the [[Frequency]] of each character                             |      1 |   true   | primary    |
| Use a [[For Loop]] to count characters from both [[String]]s into the [[Hashmap]]          |      1 |   true   | primary    |
| Return true only when both [[String]]s have the same character [[Frequency]]               |      1 |   true   | primary    |
