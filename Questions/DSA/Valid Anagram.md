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

[[Frequency Count]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Build a character [[Frequency Count]] for both [[String]]s | 2 | true | primary |
| Compare frequencies (or a single count map with increments/decrements) | 2 | true | primary |
| Use a [[Hashmap]] (or fixed alphabet array) to store counts | 1 | false | supporting |
