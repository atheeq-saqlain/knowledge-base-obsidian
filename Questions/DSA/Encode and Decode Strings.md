---
slug: dsa-encode-and-decode-strings
questionType:
---

# Encode and Decode Strings

## Statement

### Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

```java
String encode(List<String> strs) {
    // ... your code
    return encoded_string;
}
```

Machine 2 (receiver) has the function:

```java
List<String> decode(String encoded_string) {
    // ... your code
    return decoded_strs;
}
```

So Machine 1 does:

```java
String encoded_string = encode(strs);
```

and Machine 2 does:

```java
List<String> decoded_strs = decode(encoded_string);
```

`decoded_strs` in Machine 2 should be the same as the input `strs` in Machine 1.

Implement the `encode` and `decode` methods.

## Description

**Example 1:**

```java
Input: strs = ["Hello","World"]

Output: ["Hello","World"]
Explanation:

Solution solution = new Solution();
String encoded_string = solution.encode(strs);

// Machine 1 ---encoded_string---> Machine 2

List<String> decoded_strs = solution.decode(encoded_string);
```

**Example 2:**

```java
Input: strs = [""]

Output: [""]
```

**Constraints:**

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters

**Follow up:** Could you write a generalized algorithm to work on any possible set of characters?

## Correct Answer

```Python
class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res


sol = Solution()
encoded = sol.encode(["Hello", "World"])
decoded = sol.decode(encoded)
print(decoded)
```

## Core Concept

[[Length Prefix]]

## Assessment Checklist

| label                                                                                              | weight | required | role    |
| -------------------------------------------------------------------------------------------------- | -----: | :------: | ------- |
| Encode each [[String]] with a [[Length Prefix]] before its content                                 |      1 |   true   | primary |
| Use a [[For Loop]] to encode every [[String]] in the input [[Array]] into one [[String]]           |      1 |   true   | primary |
| Decode by reading each [[Length Prefix]], then slicing that many characters from the [[String]]    |      1 |   true   | primary |
| Round-trip correctly for empty strings and payloads that contain the separator character           |      1 |   true   |         |
