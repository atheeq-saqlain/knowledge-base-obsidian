---
slug: dsa-two-sum
questionType:
---
# Two Sum

## Statement

### Two Sum

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.

You may assume that every input has exactly one pair of indices `i` and `j` that satisfy the condition.

Return the answer with the smaller index first.

## Description

**Example 1:**

```java
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
```

**Example 2:**

```java
Input: nums = [4,5,6], target = 10

Output: [0,2]
```

**Example 3:**

```java
Input: nums = [5,5], target = 10

Output: [0,1]
```

## Correct Answer

```Python
class Solution:

    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                return [dic[complement], i]
            dic[nums[i]] = i


sol = Solution()
res = sol.twoSum([3, 4, 5, 6], 7)
print(res)
```

## Core Concept

[[Hashmap]]

## Assessment Checklist

| label                                                                                                | weight | required | role       |
| ---------------------------------------------------------------------------------------------------- | -----: | :------: | ---------- |
| For each value, compute its [[Complement]] (`target - value`)                                        |      1 |   true   | primary    |
| Use a [[Hashmap]] to map each [[Array]] value to its index                                           |      1 |   true   | primary    |
| Use a [[For Loop]] to scan the [[Array]] once                                                        |      1 |   true   | primary    |
| Look up whether the [[Complement]] already exists in the [[Hashmap]] before storing the current value |      1 |   true   | primary    |
| Return the two indices with the smaller index first                                                  |      1 |   true   |            |
