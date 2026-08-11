---
slug: dsa-products-of-array-except-self
questionType:
---

# Products of Array Except Self

## Statement

### Products of Array Except Self

Given an integer array `nums`, return an array `output` where `output[i]` is the product of all the elements of `nums` except `nums[i]`.

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

## Description

**Example 1:**

```java
Input: nums = [1,2,4,6]

Output: [48,24,12,8]
```

**Example 2:**

```java
Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
```

**Constraints:**

- `2 <= nums.length <= 1000`
- `-20 <= nums[i] <= 20`

## Correct Answer

```Python
class Solution:

    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output


sol = Solution()
res = sol.productExceptSelf([1, 2, 4, 6])
print(res)
```

## Core Concept

[[Prefix Product]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Apply [[Prefix Product]] (and suffix) without division | 2 | true | primary |
| Combine left and right products per index | 2 | true | primary |
| State the [[Contiguous Product Prefix Suffix]] idea | 1 | false | supporting |
