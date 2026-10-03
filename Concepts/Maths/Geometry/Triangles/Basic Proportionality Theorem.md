---
code: C-2609221829-MSXGC1XK
kind: schema
---
# Basic Proportionality Theorem

## Definition

If a line is drawn parallel to one side of a triangle intersecting the other two sides in distinct points, then those other two sides are divided in the same ratio (Thales’ theorem / BPT).

## Description

In ΔABC with DE ∥ BC (D on AB, E on AC), AD/DB = AE/EC. A useful rearrangement is AD/AB = AE/AC.

Proof outline: join BE and CD; drop perpendiculars from E to AB and from D to AC. Area ratios with common height give ar(ADE)/ar(BDE) = AD/DB and ar(ADE)/ar(DEC) = AE/EC. Triangles BDE and DEC have equal areas (same base DE between the same parallels), so AD/DB = AE/EC.

Applications: finding missing segments; proving mid-point results; ratios on trapezium sides and diagonals. The converse tests whether a line is parallel from equal ratios.

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="320" height="240" viewBox="0 0 320 240">
  <rect width="320" height="240" fill="#f8fafc" stroke="#e2e8f0"/>
  <polygon points="160,28 40,200 280,200" fill="#fff" stroke="#0f172a" stroke-width="2.5"/>
  <line x1="100" y1="114" x2="220" y2="114" stroke="#0284c7" stroke-width="2.5"/>
  <text x="154" y="20" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">A</text>
  <text x="24" y="216" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">B</text>
  <text x="284" y="216" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="bold" fill="#0f172a">C</text>
  <text x="80" y="112" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="bold" fill="#0284c7">D</text>
  <text x="224" y="112" font-family="Segoe UI, Arial, sans-serif" font-size="14" font-weight="bold" fill="#0284c7">E</text>
</svg>
```
