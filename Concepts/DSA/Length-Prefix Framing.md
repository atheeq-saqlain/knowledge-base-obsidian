---
slug: dsa-length-prefix-framing
kind: principle
---
# Length-Prefix Framing

## Definition

Variable-length payloads can be framed by writing a length then the bytes so a decoder knows exact slice bounds. Requires: [[Length Prefix Encoding]].

## Description

Common in network protocols and serialization; avoids ambiguous delimiters when content may contain the delimiter.
