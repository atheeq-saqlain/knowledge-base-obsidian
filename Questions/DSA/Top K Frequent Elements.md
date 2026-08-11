---
slug: dsa-top-k-frequent-elements
questionType:
---

# Top K Frequent Elements

## Statement

### Top K Frequent Elements

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

## Description

**Example 1:**

```java
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
```

**Example 2:**

```java
Input: nums = [7,7], k = 1

Output: [7]
```

**Constraints:**

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <=` number of distinct elements in `nums`

## Correct Answer

```Python
class Solution:

    def topKFrequent(self, nums, k):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


sol = Solution()
res = sol.topKFrequent([1, 2, 2, 3, 3, 3], 2)
print(res)
```

## Core Concept

[[Frequency Count]]

## Assessment Checklist

| label | weight | required | role |
| ----- | -----: | :------: | ---- |
| Compute a [[Frequency Count]] for each number | 2 | true | primary |
| Place numbers into [[Bucket by Frequency]] buckets indexed by count | 2 | true | primary |
| Collect the top k from highest frequency downward | 1 | true | primary |
| Discuss sort/heap vs buckets ([[Top-k Count Buckets Tradeoff]]) | 1 | false | supporting |
