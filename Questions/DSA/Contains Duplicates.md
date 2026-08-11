---
slug: dsa-contains-duplicates
questionType:
---

# Contains Duplicates

## Statement

### Contains Duplicates

Given an integer array `nums`, return `true` if any value appears **more than once** in the array, otherwise return `false`.

## Description

**Example 1:**

```java
Input: nums = [1, 2, 3, 3]

Output: true
```

**Example 2:**

```java
Input: nums = [1, 2, 3, 4]

Output: false
```

**Constraints:**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Correct Answer
```Python
class Solution:

    def containsDuplicate(self, A) -> bool:
        dic = {}
        for i in range(0, len(A)):
            print(i)
            if A[i] in dic:
                return True
            else:
                dic.get
                dic.update({A[i]: 1})
        return False

sol = Solution()
res = sol.containsDuplicate([1, 2, 3, 4, 1])

print(res)
```

## Core Concept

[[Hashset Membership]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Recognize duplicate detection as [[Hashset Membership]] | 1 | true | primary |
| Insert each [[Array]] value into a [[Hashset]] while scanning | 2 | true | primary |
| Return true as soon as an insert finds the value already present | 1 | true | primary |
