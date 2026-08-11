---
slug: dsa-contiguous-product-prefix-suffix
kind: principle
---
# Contiguous Product Prefix Suffix

## Definition

A product over all elements except index i equals (prefix product left of i) × (suffix product right of i). Requires: [[Prefix Product]].

## Description

Avoids division and handles zeros cleanly by separating left and right running products.
