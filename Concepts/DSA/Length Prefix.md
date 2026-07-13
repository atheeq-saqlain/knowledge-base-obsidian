---
slug: dsa-length-prefix
---

## Definition

A framing scheme that stores the **length** of the next chunk **before** the chunk itself, so the receiver can read an exact number of characters without relying on a reserved delimiter inside the data.

## Description

A common form is `length` + separator + `payload`, for example `5#Hello`. The decoder reads digits until the separator, converts them to an integer `n`, then takes the next `n` characters as the payload.

**Example:** encoding `["Hello", "World"]` as `5#Hello5#World`

| Step | Read | Meaning |
| ---- | ---- | ------- |
| 1 | `5` | next string has length 5 |
| 2 | `Hello` | first string |
| 3 | `5` | next string has length 5 |
| 4 | `World` | second string |

Because boundaries come from the declared length, the payload may contain any characters — including `#`, digits, spaces, or empty strings — without breaking decoding.

Useful whenever a list or record must travel as a single string (network messages, file formats, caches). Alternative approaches (escaping a delimiter, quoting) also work; length-prefixing avoids searching for a safe reserved character.
