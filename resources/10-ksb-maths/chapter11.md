# **Chapter 11: Introduction to Trigonometry — Study Guide**

---

## **I. Core Concepts & Trigonometric Principles**

### **1. What is Trigonometry?**

- **Etymology & Definition:** The word 'trigonometry' is derived from the Greek words **_'tri'_** (meaning three), **_'gon'_** (meaning sides), and **_'metron'_** (meaning measure) `. It is the branch of mathematics that studies the **relationships between the sides and angles of a triangle** `.
- **Historical Context:** Early astronomers used trigonometry to calculate the distances of the stars and planets from the Earth `. The first recorded use of the concept of 'sine' (originally *ardha-jya* or half-chord, later translated to *sinus*) is attributed to the great Indian mathematician **Aryabhata** in C.E. 500 in his work *Aryabhatiyam* `.

---

### **2. Trigonometric Ratios**

In a right-angled triangle, the trigonometric ratios of an acute angle express the relationship between the angle and the length of its sides `. Let \\(ABC\\) be a right triangle, right-angled at \\(B\\) `. With respect to the acute angle \\(\angle A\\) (or \\(\theta\\)) ``:

- **Hypotenuse:** The side opposite to the right angle (\\(AC\\)) ``.
- **Opposite Side:** The side facing angle \\(A\\) (\\(BC\\)) ``.
- **Adjacent Side:** The side adjacent to angle \\(A\\) (\\(AB\\)) ``.

#### **Geometric Visualisation of Right Triangle Ratios:**

```xml
<svg width="400" height="260" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .grid { stroke: #cbd5e1; stroke-width: 0.5; }
    .triangle { fill: #f0fdf4; stroke: #0f172a; stroke-width: 2.5; }
    .ratio-line { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .label { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #1e293b; }
    .label-bold { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; }
    .angle-arc { stroke: #ef4444; stroke-width: 2; fill: none; }
    .right-angle { stroke: #64748b; stroke-width: 1.5; fill: none; }
    .dot { fill: #0f172a; }
  </style>

  <!-- Right Triangle ABC -->
  <!-- A(80, 190), B(280, 190), C(280, 50) -->
  <polygon points="80,190 280,190 280,50" class="triangle"/>

  <!-- Right Angle Indicator at B -->
  <path d="M 265,190 L 265,175 L 280,175" class="right-angle"/>

  <!-- Angle Arc at A -->
  <path d="M 120,190 A 40,40 0 0,0 112,166" class="angle-arc"/>
  <text x="127" y="180" class="label-bold" style="fill:#ef4444;">θ</text>

  <!-- Dots for Vertices -->
  <circle cx="80" cy="190" r="4.5" class="dot"/>
  <circle cx="280" cy="190" r="4.5" class="dot"/>
  <circle cx="280" cy="50" r="4.5" class="dot"/>

  <!-- Labels for Vertices -->
  <text x="65" y="205" class="label-bold">A (Angle θ)</text>
  <text x="288" y="202" class="label-bold">B</text>
  <text x="282" y="42" class="label-bold">C</text>

  <!-- Side Labels with respect to Angle A -->
  <text x="180" y="210" class="label-bold" style="text-anchor: middle; fill:#475569;">Adjacent Side (AB)</text>
  <text x="295" y="125" class="label-bold" style="fill:#475569;">Opposite Side (BC)</text>
  <text x="155" y="110" class="label-bold" style="fill:#0284c7; transform: rotate(-35deg); transform-origin: 155px 110px;">Hypotenuse (AC)</text>
</svg>
```

The six core trigonometric ratios are defined as ``:

\$\$\sin \theta = \frac{\text{Opposite Side}}{\text{Hypotenuse}} = \frac{BC}{AC} \quad \text{``}\\[

\\]\cos \theta = \frac{\text{Adjacent Side}}{\text{Hypotenuse}} = \frac{AB}{AC} \quad \text{``}\\[

\\]\tan \theta = \frac{\text{Opposite Side}}{\text{Adjacent Side}} = \frac{BC}{AB} \quad \text{``}\\[

\\]\csc \theta = \frac{1}{\sin \theta} = \frac{\text{Hypotenuse}}{\text{Opposite Side}} = \frac{AC}{BC} \quad \text{``}\\[

\\]\sec \theta = \frac{1}{\cos \theta} = \frac{\text{Hypotenuse}}{\text{Adjacent Side}} = \frac{AC}{AB} \quad \text{``}\\[

\\]\cot \theta = \frac{1}{\tan \theta} = \frac{\text{Adjacent Side}}{\text{Opposite Side}} = \frac{AB}{BC} \quad \text{``}\$\$

- **Quotient Relations:** \\(\tan \theta = \frac{\sin \theta}{\cos \theta}\\) and \\(\cot \theta = \frac{\cos \theta}{\sin \theta}\\) ``.
- **Uniqueness Principle:** The values of the trigonometric ratios of an angle **do not vary with the lengths of the sides of the triangle** if the angle remains the same ``.
- **Scale Limits:** Because the hypotenuse is the longest side in a right triangle, the value of \\(\sin A\\) or \\(\cos A\\) is **always less than or equal to 1** `, while the value of \\(\sec A\\) or \\(\csc A\\) is **always greater than or equal to 1** `.

---

## **II. Trigonometric Ratios of Specific Angles**

By using geometry, we derive the exact values of trigonometric ratios for standard angles (\\(0^\circ, 30^\circ, 45^\circ, 60^\circ,\\) and \\(90^\circ\\)) ``:

| \\(\angle A\\)   | \\(0^\circ\\) `` |    \\(30^\circ\\) ``     |    \\(45^\circ\\) ``     |    \\(60^\circ\\) ``     | \\(90^\circ\\) `` |
| :--------------- | :--------------: | :----------------------: | :----------------------: | :----------------------: | :---------------: |
| **\\(\sin A\\)** |     \\(0\\)      |    \\(\frac{1}{2}\\)     | \\(\frac{1}{\sqrt{2}}\\) | \\(\frac{\sqrt{3}}{2}\\) |      \\(1\\)      |
| **\\(\cos A\\)** |     \\(1\\)      | \\(\frac{\sqrt{3}}{2}\\) | \\(\frac{1}{\sqrt{2}}\\) |    \\(\frac{1}{2}\\)     |      \\(0\\)      |
| **\\(\tan A\\)** |     \\(0\\)      | \\(\frac{1}{\sqrt{3}}\\) |         \\(1\\)          |      \\(\sqrt{3}\\)      |   _Not defined_   |
| **\\(\csc A\\)** |  _Not defined_   |         \\(2\\)          |      \\(\sqrt{2}\\)      | \\(\frac{2}{\sqrt{3}}\\) |      \\(1\\)      |
| **\\(\sec A\\)** |     \\(1\\)      | \\(\frac{2}{\sqrt{3}}\\) |      \\(\sqrt{2}\\)      |         \\(2\\)          |   _Not defined_   |
| **\\(\cot A\\)** |  _Not defined_   |      \\(\sqrt{3}\\)      |         \\(1\\)          | \\(\frac{1}{\sqrt{3}}\\) |      \\(0\\)      |

- **Observation:** As \\(\angle A\\) increases from \\(0^\circ\\) to \\(90^\circ\\), **\\(\sin A\\) increases from \\(0\\) to \\(1\\)**, and **\\(\cos A\\) decreases from \\(1\\) to \\(0\\)** ``.

---

## **III. Trigonometric Ratios of Complementary Angles**

Two angles are complementary if their sum equals \\(90^\circ\\) `. In right-angled triangle \\(ABC\\), \\(\angle A\\) and \\(\angle C\\) are complementary, meaning \\(\angle C = 90^\circ - A\\) `.

#### **Trigonometric Complementary Pairs:**

```xml
<svg width="450" height="150" viewBox="0 0 450 150" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .node-box { fill: #ffffff; stroke: #cbd5e1; stroke-width: 1.5; }
    .label-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; fill: #0f172a; font-weight: bold; text-anchor: middle; }
    .label-formula { font-family: 'Consolas', monospace; font-size: 12px; fill: #475569; text-anchor: middle; }
    .relation-arrow { stroke: #8b5cf6; stroke-width: 2; fill: none; marker-end: url(#arrow-purple); marker-start: url(#arrow-purple); }
  </style>
  <defs>
    <marker id="arrow-purple" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#8b5cf6"/>
    </marker>
  </defs>

  <!-- Pair 1: Sin <-> Cos -->
  <g transform="translate(15, 20)">
    <rect x="0" y="0" width="110" height="90" rx="6" class="node-box"/>
    <text x="55" y="30" class="label-title" style="fill:#0284c7;">sin &amp; cos</text>
    <text x="55" y="55" class="label-formula">sin(90°-A)</text>
    <text x="55" y="72" class="label-formula">= cos A</text>
  </g>

  <!-- Double arrow 1 -->
  <path d="M 135,65 L 155,65" class="relation-arrow"/>

  <!-- Pair 2: Tan <-> Cot -->
  <g transform="translate(170, 20)">
    <rect x="0" y="0" width="110" height="90" rx="6" class="node-box"/>
    <text x="55" y="30" class="label-title" style="fill:#16a34a;">tan &amp; cot</text>
    <text x="55" y="55" class="label-formula">tan(90°-A)</text>
    <text x="55" y="72" class="label-formula">= cot A</text>
  </g>

  <!-- Double arrow 2 -->
  <path d="M 290,65 L 310,65" class="relation-arrow"/>

  <!-- Pair 3: Sec <-> Csc -->
  <g transform="translate(325, 20)">
    <rect x="0" y="0" width="110" height="90" rx="6" class="node-box"/>
    <text x="55" y="30" class="label-title" style="fill:#ef4444;">sec &amp; csc</text>
    <text x="55" y="55" class="label-formula">sec(90°-A)</text>
    <text x="55" y="72" class="label-formula">= csc A</text>
  </g>
</svg>
```

The complementary relationships are defined as ``:

\$\$\sin(90^\circ - A) = \cos A \quad\text{and}\quad \cos(90^\circ - A) = \sin A \quad \text{``}\\[

\\]\tan(90^\circ - A) = \cot A \quad\text{and}\quad \cot(90^\circ - A) = \tan A \quad \text{``}\\[

\\]\sec(90^\circ - A) = \csc A \quad\text{and}\quad \csc(90^\circ - A) = \sec A \quad \text{``}\$\$

---

## **IV. Trigonometric Identities**

A trigonometric identity is an equation involving trigonometric ratios that is true for all permissible values of its angle ``.

#### **Geometric Proof on the Unit Circle:**

In the first quadrant of a coordinate plane with a unit radius \\(OP = 1\\), the coordinates of \\(P(x, y)\\) are represented by \\((\cos \theta, \sin \theta)\\):

```xml
<svg width="300" height="260" viewBox="0 0 300 260" xmlns="http://www.w3.org/2000/svg" style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; display: block; margin: 20px auto;">
  <style>
    .axis { stroke: #475569; stroke-width: 1.5; }
    .grid-line { stroke: #cbd5e1; stroke-dasharray: 2 2; }
    .arc { fill: none; stroke: #94a3b8; stroke-width: 1.5; }
    .vector { stroke: #0284c7; stroke-width: 2.5; fill: none; }
    .trig-y { stroke: #ef4444; stroke-width: 2.5; fill: none; }
    .trig-x { stroke: #16a34a; stroke-width: 2.5; fill: none; }
    .label-math { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; }
  </style>

  <!-- Axes (Origin at 60, 200) -->
  <line x1="60" y1="20" x2="60" y2="220" class="axis"/>
  <line x1="40" y1="200" x2="260" y2="200" class="axis"/>

  <!-- Circular Arc (Radius = 160) -->
  <path d="M 220,200 A 160,160 0 0,0 60,40" class="arc"/>

  <!-- Vector OP to (156, 104) -> absolute x=156, y=104 -->
  <!-- At angle 37 degrees: cos(37) = 0.8 (128px), sin(37) = 0.6 (96px) -->
  <!-- Coordinate of P: x = 60 + 128 = 188, y = 200 - 96 = 104 -->
  <polygon points="60,200 188,200 188,104" fill="none" stroke="#64748b" stroke-dasharray="3 3"/>
  <line x1="60" y1="200" x2="188" y2="104" class="vector"/>

  <!-- Sine and Cosine Highlights -->
  <line x1="188" y1="200" x2="188" y2="104" class="trig-y"/> <!-- sin -->
  <line x1="60" y1="200" x2="188" y2="200" class="trig-x"/> <!-- cos -->

  <!-- Angle arc at O -->
  <path d="M 90,200 A 30,30 0 0,0 84,182" fill="none" stroke="#ef4444" stroke-width="1.5"/>

  <!-- Dots -->
  <circle cx="188" cy="104" r="4.5" fill="#0f172a"/>
  <circle cx="60" cy="200" r="4" fill="#0f172a"/>

  <!-- Text Labels -->
  <text x="95" y="193" style="fill:#ef4444;" class="label-math">θ</text>
  <text x="45" y="215" style="fill:#0f172a;" class="label-math">O</text>
  <text x="195" y="100" style="fill:#0f172a;" class="label-math">P(cos θ, sin θ)</text>
  <text x="115" y="140" style="fill:#0284c7;" class="label-math">OP = 1</text>
  <text x="195" y="155" style="fill:#ef4444;" class="label-math">sin θ</text>
  <text x="110" y="218" style="fill:#16a34a;" class="label-math">cos θ</text>
</svg>
```

Applying the Pythagoras theorem directly to the right-angled triangle coordinates gives the **three fundamental trigonometric identities** ``:

\$\$\sin^2 A + \cos^2 A = 1 \quad (\text{for } 0^\circ \le A \le 90^\circ) \quad \text{``}\\[

\\]1 + \tan^2 A = \sec^2 A \quad (\text{for } 0^\circ \le A < 90^\circ) \quad \text{``}\\[

\\]1 + \cot^2 A = \csc^2 A \quad (\text{for } 0^\circ < A \le 90^\circ) \quad \text{``}\$\$

---

## **V. Example Problems & Step-by-Step Solutions**

### **Example 1**

**Problem:** Given \\(\tan A = \frac{4}{3}\\), find the other trigonometric ratios of the angle \\(A\\) ``.

- **Solution:**
  - \\(\tan A = \frac{BC}{AB} = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{4}{3}\\) `. Let \\(BC = 4k\\) and \\(AB = 3k\\), where \\(k > 0\\) `.
  - Using the Pythagoras Theorem:
    \$\$AC = \sqrt{AB^2 + BC^2} = \sqrt{(3k)^2 + (4k)^2} = \sqrt{25k^2} = 5k \quad \text{``}\$\$
  - Find the remaining ratios using their definitions `:
\sin A = \frac{BC}{AC} = \frac{4k}{5k} = \frac{4}{5} \quad\text{and}\quad \cos A = \frac{AB}{AC} = \frac{3k}{5k} = \frac{3}{5} \quad \text{`}\\[
    \\]\csc A = \frac{1}{\sin A} = \frac{5}{4}, \quad \sec A = \frac{1}{\cos A} = \frac{5}{3}, \quad \cot A = \frac{1}{\tan A} = \frac{3}{4} \quad \text{``}\$\$

---

### **Example 2**

**Problem:** In right triangle \\(ABC\\) angled at \\(B\\), if \\(\tan A = 1\\), verify that \\(2 \sin A \cos A = 1\\) ``.

- **Solution:**
  - \\(\tan A = \frac{BC}{AB} = 1 \implies BC = AB\\) `. Let \\(AB = BC = k\\) `.
  - By Pythagoras theorem:
    \$\$AC = \sqrt{AB^2 + BC^2} = \sqrt{k^2 + k^2} = k\sqrt{2} \quad \text{``}\$\$
  - Calculate \\(\sin A\\) and \\(\cos A\\) `:
\sin A = \frac{BC}{AC} = \frac{k}{k\sqrt{2}} = \frac{1}{\sqrt{2}} \quad\text{and}\quad \cos A = \frac{AB}{AC} = \frac{k}{k\sqrt{2}} = \frac{1}{\sqrt{2}} \quad \text{`}\$\$
  - Verify `:
2 \sin A \cos A = 2 \left(\frac{1}{\sqrt{2}}\right)\left(\frac{1}{\sqrt{2}}\right) = 2 \left(\frac{1}{2}\right) = 1 \quad \text{(Verified) `}\$\$

---

### **Example 3**

**Problem:** In \\(\Delta OPQ\\), right-angled at \\(P\\), \\(OP = 7\text{ cm}\\) and \\(OQ - PQ = 1\text{ cm}\\). Determine the values of \\(\sin Q\\) and \\(\cos Q\\) ``.

- **Solution:**
  - Using Pythagoras theorem in right triangle \\(OPQ\\) `:
OQ^2 = OP^2 + PQ^2 \implies (1 + PQ)^2 = 7^2 + PQ^2 \quad \text{(since } OQ = 1 + PQ) \quad \text{`}\\[
    \\]1 + PQ^2 + 2PQ = 49 + PQ^2 \implies 1 + 2PQ = 49 \quad \text{`}\\[
\\]2PQ = 48 \implies PQ = 24\text{ cm} \quad \text{`}\$\$
  - Find \\(OQ\\) `:
\$\$OQ = 1 + 24 = 25\text{ cm} \quad \text{`}\$\$
  - Calculate ratios `:
\sin Q = \frac{OP}{OQ} = \frac{7}{25} \quad\text{and}\quad \cos Q = \frac{PQ}{OQ} = \frac{24}{25} \quad \text{`}\$\$

---

### **Example 4**

**Problem:** In \\(\Delta ABC\\), right-angled at \\(B\\), \\(AB = 5\text{ cm}\\) and \\(\angle ACB = 30^\circ\\). Determine the lengths of the sides \\(BC\\) and \\(AC\\) ``.

- **Solution:**
  - To find the adjacent side \\(BC\\), use \\(\tan C\\) `:
\tan 30^\circ = \frac{AB}{BC} \implies \frac{1}{\sqrt{3}} = \frac{5}{BC} \implies BC = 5\sqrt{3}\text{ cm} \quad \text{`}\$\$
  - To find the hypotenuse \\(AC\\), use \\(\sin C\\) `:
\sin 30^\circ = \frac{AB}{AC} \implies \frac{1}{2} = \frac{5}{AC} \implies AC = 10\text{ cm} \quad \text{`}\$\$

---

### **Example 5**

**Problem:** If \\(\sin(A - B) = \frac{1}{2}\\) and \\(\cos(A + B) = \frac{1}{2}\\), where \\(0^\circ < A + B \le 90^\circ\\) and \\(A > B\\), solve for \\(A\\) and \\(B\\) ``.

- **Solution:**
  - Since \\(\sin(A - B) = \frac{1}{2}\\), and we know \\(\sin 30^\circ = \frac{1}{2}\\) `:
\$\$A - B = 30^\circ \quad \text{--- (Eq. 1) `}\$\$
  - Since \\(\cos(A + B) = \frac{1}{2}\\), and we know \\(\cos 60^\circ = \frac{1}{2}\\) `:
\$\$A + B = 60^\circ \quad \text{--- (Eq. 2) `}\$\$
  - Add (Eq. 1) and (Eq. 2) `:
\$\$(A - B) + (A + B) = 30^\circ + 60^\circ \implies 2A = 90^\circ \implies A = 45^\circ \quad \text{`}\$\$
  - Substitute \\(A = 45^\circ\\) into (Eq. 2) `:
45^\circ + B = 60^\circ \implies B = 15^\circ \quad \text{`}\$\$
  - **Answer:** \\(A = 45^\circ\\), \\(B = 15^\circ\\) ``.

---

### **Example 6**

**Problem:** Prove the identity: \\(\sec A(1 - \sin A)(\sec A + \tan A) = 1\\) ``.

- **Solution:**
  - Express the LHS in terms of sines and cosines `:
\text{LHS} = \sec A(1 - \sin A)(\sec A + \tan A) = \left(\frac{1}{\cos A}\right)(1 - \sin A)\left(\frac{1}{\cos A} + \frac{\sin A}{\cos A}\right) \quad \text{`}\$\$
  - Simplify the fractions `:
\text{LHS} = \frac{1 - \sin A}{\cos A} \left(\frac{1 + \sin A}{\cos A}\right) = \frac{(1 - \sin A)(1 + \sin A)}{\cos^2 A} \quad \text{`}\\[
    \\]\text{LHS} = \frac{1 - \sin^2 A}{\cos^2 A} \quad \text{``}\$\$
  - Apply the identity \\(1 - \sin^2 A = \cos^2 A\\) `:
\text{LHS} = \frac{\cos^2 A}{\cos^2 A} = 1 = \text{RHS} \quad \text{(Proven) `}\$\$

---

## **VI. Textbook Exercises**

### **EXERCISE 11.1**

1.  In \\(\Delta ABC\\), right-angled at \\(B\\), \\(AB = 24\text{ cm}\\) and \\(BC = 7\text{ cm}\\) ``. Determine:
    - (i) \\(\sin A, \cos A\\) ``
    - (ii) \\(\sin C, \cos C\\) ``
2.  In right-angled triangle \\(PQR\\), if \\(PQ = 12\text{ cm}\\) and \\(PR = 13\text{ cm}\\), find the value of \\(\tan P - \cot R\\) ``.
3.  If \\(\sin A = \frac{3}{4}\\), calculate \\(\cos A\\) and \\(\tan A\\) ``.
4.  Given \\(15 \cot A = 8\\), find the values of \\(\sin A\\) and \\(\sec A\\) ``.
5.  Given \\(\sec \theta = \frac{13}{12}\\), calculate all other trigonometric ratios ``.
6.  If \\(\angle A\\) and \\(\angle B\\) are acute angles such that \\(\cos A = \cos B\\), then prove that \\(\angle A = \angle B\\) ``.
7.  If \\(\cot \theta = \frac{7}{8}\\), evaluate:
    - (i) \\(\frac{(1 + \sin \theta)(1 - \sin \theta)}{(1 + \cos \theta)(1 - \cos \theta)}\\) ``
    - (ii) \\(\cot^2 \theta\\) ``
8.  If \\(3 \cot A = 4\\), check whether \\(\frac{1 - \tan^2 A}{1 + \tan^2 A} = \cos^2 A - \sin^2 A\\) or not ``.
9.  In triangle \\(ABC\\), right-angled at \\(B\\), if \\(\tan A = \frac{1}{\sqrt{3}}\\), find the value of:
    - (i) \\(\sin A \cos C + \cos A \sin C\\) ``
    - (ii) \\(\cos A \cos C - \sin A \sin C\\) ``
10. In \\(\Delta PQR\\), right-angled at \\(Q\\), \\(PR + QR = 25\text{ cm}\\) and \\(PQ = 5\text{ cm}\\). Determine the values of \\(\sin P, \cos P,\\) and \\(\tan P\\) ``.

---

### **EXERCISE 11.2**

1.  **Evaluate the following:**
    - (i) \\(\sin 60^\circ \cos 30^\circ + \sin 30^\circ \cos 60^\circ\\) ``
    - (ii) \\(2 \tan^2 45^\circ + \cos^2 30^\circ - \sin^2 60^\circ\\) ``
    - (iii) \\(\frac{\cos 45^\circ}{\sec 30^\circ + \csc 30^\circ}\\) ``
    - (iv) \\(\frac{\sin 30^\circ + \tan 45^\circ - \csc 60^\circ}{\sec 30^\circ + \cos 60^\circ + \cot 45^\circ}\\) ``
    - (v) \\(\frac{5 \cos^2 60^\circ + 4 \sec^2 30^\circ - \tan^2 45^\circ}{\sin^2 30^\circ + \cos^2 30^\circ}\\) ``
2.  Choose the correct option and justify your choice:
    - (i) \\(\frac{2 \tan 30^\circ}{1 + \tan^2 30^\circ} =\\)
      _(A) \\(\sin 60^\circ\\) \quad (B) \\(\cos 60^\circ\\) \quad (C) \\(\tan 60^\circ\\) \quad (D) \\(\sin 30^\circ\\)_ ``
    - (ii) \\(\frac{1 - \tan^2 45^\circ}{1 + \tan^2 45^\circ} =\\)
      _(A) \\(\tan 90^\circ\\) \quad (B) \\(1\\) \quad (C) \\(\sin 45^\circ\\) \quad (D) \\(0\\)_ ``
    - (iii) \\(\sin 2A = 2 \sin A\\) is true when \\(A =\\)
      _(A) \\(0^\circ\\) \quad (B) \\(30^\circ\\) \quad (C) \\(45^\circ\\) \quad (D) \\(60^\circ\\)_ ``
    - (iv) \\(\frac{2 \tan 30^\circ}{1 - \tan^2 30^\circ} =\\)
      _(A) \\(\cos 60^\circ\\) \quad (B) \\(\sin 60^\circ\\) \quad (C) \\(\tan 60^\circ\\) \quad (D) \\(\sin 30^\circ\\)_ ``
3.  If \\(\tan (A + B) = \sqrt{3}\\) and \\(\tan (A - B) = \frac{1}{\sqrt{3}}\\); \\(0^\circ < A + B \le 90^\circ\\); \\(A > B\\), find \\(A\\) and \\(B\\) ``.

---

### **EXERCISE 11.3**

1.  **Evaluate:**
    - (i) \\(\frac{\sin 18^\circ}{\cos 72^\circ}\\) ``
    - (ii) \\(\frac{\tan 26^\circ}{\cot 64^\circ}\\) ``
    - (iii) \\(\cos 48^\circ - \sin 42^\circ\\) ``
    - (iv) \\(\csc 31^\circ - \sec 59^\circ\\) ``
2.  **Show that:**
    - (i) \\(\tan 48^\circ \tan 23^\circ \tan 42^\circ \tan 67^\circ = 1\\) ``
    - (ii) \\(\cos 38^\circ \cos 52^\circ - \sin 38^\circ \sin 52^\circ = 0\\) ``
3.  If \\(\tan 2A = \cot(A - 18^\circ)\\), where \\(2A\\) is an acute angle, find the value of \\(A\\) ``.
4.  If \\(\tan A = \cot B\\), prove that \\(A + B = 90^\circ\\) ``.
5.  If \\(\sec 4A = \csc(A - 20^\circ)\\), where \\(4A\\) is an acute angle, find the value of \\(A\\) ``.
6.  If \$A, B\$ and \$C\\( are interior angles of a triangle \\)ABC\\(, then show that:
    \\)\$\sin\left(\frac{B+C}{2}\right) = \cos\frac{A}{2} \quad \text{``}\$\$
7.  Express \\(\sin 67^\circ + \cos 75^\circ\\) in terms of trigonometric ratios of angles between \\(0^\circ\\) and \\(45^\circ\\) ``.

---

### **EXERCISE 11.4**

1.  Express the trigonometric ratios \\(\sin A, \sec A\\) and \\(\tan A\\) in terms of \\(\cot A\\) ``.
2.  Write all the other trigonometric ratios of \\(\angle A\\) in terms of \\(\sec A\\) ``.
3.  **Evaluate:**
    - (i) \\(\frac{\sin^2 63^\circ + \sin^2 27^\circ}{\cos^2 17^\circ + \cos^2 73^\circ}\\) ``
    - (ii) \\(\sin 25^\circ \cos 65^\circ + \cos 25^\circ \sin 65^\circ\\) ``
4.  Choose the correct option and justify your choice:
    - (i) \\(9 \sec^2 A - 9 \tan^2 A =\\)
      _(A) \\(1\\) \quad (B) \\(9\\) \quad (C) \\(8\\) \quad (D) \\(0\\)_ ``
    - (ii) \\((1 + \tan \theta + \sec \theta)(1 + \cot \theta - \csc \theta) =\\)
      _(A) \\(0\\) \quad (B) \\(1\\) \quad (C) \\(2\\) \quad (D) \\(-1\\)_ ``
    - (iii) \\((\sec A + \tan A)(1 - \sin A) =\\)
      _(A) \\(\sec A\\) \quad (B) \\(\sin A\\) \quad (C) \\(\csc A\\) \quad (D) \\(\cos A\\)_ ``
    - (iv) \\(\frac{1 + \tan^2 A}{1 + \cot^2 A} =\\)
      _(A) \\(\sec^2 A\\) \quad (B) \\(-1\\) \quad (C) \\(\cot^2 A\\) \quad (D) \\(\tan^2 A\\)_ ``
5.  **Prove the following identities, where the angles involved are acute angles for which the expressions are defined:**
    - (i) \\((\csc \theta - \cot \theta)^2 = \frac{1 - \cos \theta}{1 + \cos \theta}\\) ``
    - (ii) \\(\frac{\cos A}{1 + \sin A} + \frac{1 + \sin A}{\cos A} = 2 \sec A\\) ``
    - (iii) \\(\frac{\tan \theta}{1 - \cot \theta} + \frac{\cot \theta}{1 - \tan \theta} = 1 + \sec \theta \csc \theta\\) ``
    - (iv) \\(\frac{1 + \sec A}{\sec A} = \frac{\sin^2 A}{1 - \cos A}\\) ``
    - (v) \\(\frac{\cos A - \sin A + 1}{\cos A + \sin A - 1} = \csc A + \cot A\\), using the identity \\(\csc^2 A = 1 + \cot^2 A\\) ``
    - (vi) \\(\sqrt{\frac{1 + \sin A}{1 - \sin A}} = \sec A + \tan A\\) ``
    - (vii) \\(\frac{\sin \theta - 2 \sin^3 \theta}{2 \cos^3 \theta - \cos \theta} = \tan \theta\\) ``
    - (viii) \\((\sin A + \csc A)^2 + (\cos A + \sec A)^2 = 7 + \tan^2 A + \cot^2 A\\) ``
    - (ix) \\((\csc A - \sin A)(\sec A - \cos A) = \frac{1}{\tan A + \cot A}\\) ``
    - (x) \\(\left(\frac{1 + \tan^2 A}{1 + \cot^2 A}\right) = \left(\frac{1 - \tan A}{1 - \cot A}\right)^2 = \tan^2 A\\) ``

---

📐 **I can compile this comprehensive trigonometry study guide into a polished formula PDF sheet or write a custom Python script in our workspace to evaluate complex trigonometric identity proofs. What would you like to build next?**
