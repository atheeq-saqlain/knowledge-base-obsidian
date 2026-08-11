---
slug: dsa-hashset-membership
kind: schema
---
# Hashset Membership

## Definition

A technique that answers “have I seen this value?” using a [[Hashset]] (or set-like structure) for O(1) average membership tests. Requires: [[Hashset]].

## Description

Used for duplicate detection and consecutive-sequence problems where presence matters more than counts. Prefer a set when you only need membership, not frequencies.
