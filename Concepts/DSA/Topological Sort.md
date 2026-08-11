---
slug: dsa-topological-sort
kind: schema
---

# Topological Sort

## Definition

An ordering of vertices in a directed acyclic graph such that every edge goes from earlier to later in the order. Requires: [[Graph]].

## Description

Used for course prerequisites and build dependency ordering. Detects cycles when no valid order exists.
