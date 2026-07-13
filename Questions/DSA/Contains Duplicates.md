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
[[Hashmap]]

## Assessment Checklist
| label                                                                      | weight | required | role    |
| -------------------------------------------------------------------------- | -----: | :------: | ------- |
| Use [[Hashmap]] to store the [[Frequency]] of the numbers in the [[Array]] |      1 |   true   | primary |
| Use [[For Loop]] to build the [[Hashmap]]                                  |      1 |   true   | primary |
| Check and return the result if the frequency of any number is >1           |      1 |   true   |         |
