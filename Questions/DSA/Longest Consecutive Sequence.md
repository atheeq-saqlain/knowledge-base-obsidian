---
slug: dsa-longest-consecutive-sequence
questionType:
---

# Longest Consecutive Sequence

## Statement

### Longest Consecutive Sequence

Given an array of integers `nums`, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

## Description

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

**Example 1:**

```java
Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
```

**Example 2:**

```java
Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
```

**Constraints:**

- `0 <= nums.length <= 1000`
- `-10^9 <= nums[i] <= 10^9`

## Correct Answer

```Python
class Solution:

    def longestConsecutive(self, nums):
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest


sol = Solution()
res = sol.longestConsecutive([2, 20, 4, 10, 3, 4, 5])
print(res)
```

## Core Concept

[[Hashset Membership]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Use [[Hashset Membership]] to store all numbers | 2 | true | primary |
| Only start a streak when `x-1` is not in the set | 2 | true | primary |
| Extend the streak while `x+1` remains present; track max length | 1 | true | primary |
